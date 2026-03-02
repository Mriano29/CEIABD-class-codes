# app.py
from flask import Flask, request, session, redirect, url_for, render_template_string
import requests
import os
import uuid
from pathlib import Path
from transformers import pipeline
import soundfile as sf
import torch
from TTS.api import TTS  # Coqui TTS

LMSTUDIO_BASE_URL = os.environ.get(
    "LMSTUDIO_BASE_URL", "http://127.0.0.1:1234/v1")
MODEL_ID = os.environ.get("LMSTUDIO_MODEL", "google/gemma-3-4b")

# Modelo TTS en español
TTS_MODEL = os.environ.get("TTS_MODEL", "tts_models/es/css10/vits")

# ASR Whisper
ASR_BACKEND = os.environ.get("ASR_BACKEND", "hf")  # default: hf
WHISPER_MODEL = os.environ.get("WHISPER_MODEL", "openai/whisper-small")

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "dev-secret-key-change-me")

# Asegura carpeta static
Path("PRO/CÓDIGO/static").mkdir(exist_ok=True)

# Carga el modelo TTS UNA VEZ al arrancar
tts = TTS(model_name=TTS_MODEL, progress_bar=False, gpu=False)

# ASR (Whisper HF)
asr = pipeline(
    "automatic-speech-recognition",
    model=WHISPER_MODEL,
    generate_kwargs={"language": "spanish", "task": "transcribe"},
)

# Función para transcribir audio WAV sin ffmpeg


def transcribe_audio(file_path: str) -> str:
    try:
        # Leer WAV
        audio, sr = sf.read(file_path, dtype='float32') 
        # Flatten si es stereo (Whisper HF espera mono)
        if audio.ndim > 1:
            audio = audio.mean(axis=1)
        # Pasar array directamente al pipeline
        result = asr(audio)
        return result["text"]
    except Exception as e:
        return f"[Error ASR] {e}"


# Resto de tu HTML (solo cambiamos accept del input a WAV)
HTML = """
<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Chat LM Studio (Flask)</title>
  <style>
    body { font-family: system-ui, Arial; max-width: 900px; margin: 24px auto; padding: 0 12px; }
    .box { border: 1px solid #ddd; border-radius: 10px; padding: 14px; }
    .row { margin: 10px 0; }
    .msg { padding: 10px 12px; border-radius: 10px; margin: 8px 0; white-space: pre-wrap; }
    .user { background: #eef6ff; }
    .assistant { background: #f6f6f6; }
    textarea { width: 100%; height: 90px; }
    button { padding: 10px 14px; cursor: pointer; }
    .meta { color:#666; font-size: 12px; }
  </style>
</head>
<body>
  <h1>Chat local con LM Studio</h1>
  <p class="meta">Base URL: {{ base_url }} · Modelo: {{ model_id }} · TTS: {{ tts_model }}</p>

  <div class="box">
    {% for m in messages %}
      <div class="msg {{ 'user' if m.role=='user' else 'assistant' }}">
        <b>{{ 'Tú' if m.role=='user' else 'IA' }}:</b> {{ m.content }}
      </div>
    {% endfor %}
  </div>

  {% if last_audio %}
    <div class="row">
      <p class="meta">Audio generado:</p>
      <audio controls autoplay>
        <source src="{{ last_audio }}" type="audio/wav">
      </audio>
    </div>
  {% endif %}

  <div class="row">
    <form method="post" action="{{ url_for('send') }}" enctype="multipart/form-data">
      <textarea name="prompt" placeholder="Escribe aquí..."></textarea>
      <div style="margin-top:10px;">
        <!-- Solo WAV -->
        <input type="file" name="audio" accept=".wav,audio/wav" />
        <button type="submit" formaction="{{ url_for('asr_endpoint') }}">
          Enviar audio
        </button>
      </div>
      <div style="display:flex; gap:10px; margin-top:10px;">
        <button type="submit">Enviar</button>
        <button type="submit" formaction="{{ url_for('reset') }}">Reset</button>
      </div>
    </form>
  </div>

  <p class="meta">
    Tip: si quieres cambiar modelo/host sin tocar código:
    <code>LMSTUDIO_BASE_URL</code> y <code>LMSTUDIO_MODEL</code> en variables de entorno.
  </p>
</body>
</html>
"""

# Función TTS


def local_tts_to_wav(text: str) -> str:
    fname = f"{uuid.uuid4().hex}.wav"
    fpath = Path("PRO/CÓDIGO/static") / fname
    tts.tts_to_file(text=text, file_path=str(fpath))
    return f"/static/{fname}"

# Función LM Studio


def lmstudio_chat(messages, temperature=0.7, max_tokens=512):
    url = f"{LMSTUDIO_BASE_URL}/chat/completions"
    payload = {
        "model": MODEL_ID,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
        "stream": False
    }
    headers = {"Content-Type": "application/json"}
    r = requests.post(url, json=payload, headers=headers, timeout=120)
    r.raise_for_status()
    data = r.json()
    return data["choices"][0]["message"]["content"]


@app.get("/")
def index():
    if "messages" not in session:
        session["messages"] = [
            {"role": "system", "content": "Eres un asistente útil y conciso."}]
    visible = [m for m in session["messages"] if m["role"] != "system"]
    return render_template_string(
        HTML,
        messages=visible,
        base_url=LMSTUDIO_BASE_URL,
        model_id=MODEL_ID,
        tts_model=TTS_MODEL,
        last_audio=session.get("last_audio")
    )


@app.post("/send")
def send():
    prompt = (request.form.get("prompt") or "").strip()
    if not prompt:
        return redirect(url_for("index"))
    session.setdefault(
        "messages", [{"role": "system", "content": "Eres un asistente útil y conciso."}])
    session["messages"].append({"role": "user", "content": prompt})
    try:
        answer = lmstudio_chat(session["messages"])
    except requests.RequestException as e:
        answer = f"[Error llamando a LM Studio] {e}"
    session["messages"].append({"role": "assistant", "content": answer})
    try:
        session["last_audio"] = local_tts_to_wav(answer)
    except Exception as e:
        session["last_audio"] = None
        session["messages"].append(
            {"role": "assistant", "content": f"[Aviso TTS] No se pudo generar audio: {e}"})
    session.modified = True
    return redirect(url_for("index"))


@app.post("/reset")
def reset():
    session["messages"] = [
        {"role": "system", "content": "Eres un asistente útil y conciso."}]
    session["last_audio"] = None
    session.modified = True
    return redirect(url_for("index"))

@app.post("/asr")
def asr_endpoint():
    if "audio" not in request.files:
        return "No se envió audio", 400

    audio_file = request.files["audio"]
    if audio_file.filename == "":
        return "Archivo vacío", 400

    fname = f"{uuid.uuid4().hex}.wav"
    fpath = Path("PRO/CÓDIGO/static") / fname
    audio_file.save(fpath)

    # Transcribir WAV
    text = transcribe_audio(str(fpath))

    # Guardar transcripción en session
    session.setdefault("messages", [{"role": "system", "content": "Eres un asistente útil y conciso."}])
    session["messages"].append({"role": "user", "content": f"[Audio → texto] {text}"})

    # Llamamos a LM Studio para que responda
    try:
        answer = lmstudio_chat(session["messages"])
    except requests.RequestException as e:
        answer = f"[Error llamando a LM Studio] {e}"

    session["messages"].append({"role": "assistant", "content": answer})

    # Generar TTS
    try:
        session["last_audio"] = local_tts_to_wav(answer)
    except Exception as e:
        session["last_audio"] = None
        session["messages"].append({"role": "assistant", "content": f"[Aviso TTS] No se pudo generar audio: {e}"})

    session.modified = True
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
