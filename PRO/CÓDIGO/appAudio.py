
# app.py
from flask import Flask, request, session, redirect, url_for, render_template_string
import requests
import os
import uuid
from pathlib import Path

from TTS.api import TTS  # Coqui TTS

LMSTUDIO_BASE_URL = os.environ.get("LMSTUDIO_BASE_URL", "http://127.0.0.1:1234/v1")
MODEL_ID = os.environ.get("LMSTUDIO_MODEL", "google/gemma-3-4b")

# Modelo TTS en español (puedes cambiarlo más adelante)
TTS_MODEL = os.environ.get("TTS_MODEL", "tts_models/es/css10/vits")

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "dev-secret-key-change-me")

# Asegura carpeta static
Path("PRO/CÓDIGO/static").mkdir(exist_ok=True)

# Carga el modelo TTS UNA VEZ al arrancar (importante)
# gpu=False para que sea sencillo y reproducible
tts = TTS(model_name=TTS_MODEL, progress_bar=False, gpu=False)

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
    <form method="post" action="{{ url_for('send') }}">
      <textarea name="prompt" placeholder="Escribe aquí..."></textarea>
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

def local_tts_to_wav(text: str) -> str:
    """Genera un WAV en /static y devuelve la URL /static/xxxx.wav"""
    fname = f"{uuid.uuid4().hex}.wav"
    fpath = Path("PRO/CÓDIGO/static") / fname
    tts.tts_to_file(text=text, file_path=str(fpath))
    return f"/static/{fname}"

@app.get("/")
def index():
    if "messages" not in session:
        session["messages"] = [{"role": "system", "content": "Eres un asistente útil y conciso."}]
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

    session.setdefault("messages", [{"role": "system", "content": "Eres un asistente útil y conciso."}])
    session["messages"].append({"role": "user", "content": prompt})

    try:
        answer = lmstudio_chat(session["messages"])
    except requests.RequestException as e:
        answer = f"[Error llamando a LM Studio] {e}"

    session["messages"].append({"role": "assistant", "content": answer})

    # Generación de audio local (Coqui)
    try:
        session["last_audio"] = local_tts_to_wav(answer)
    except Exception as e:
        session["last_audio"] = None
        session["messages"].append({"role": "assistant", "content": f"[Aviso TTS] No se pudo generar audio: {e}"})

    session.modified = True
    return redirect(url_for("index"))

@app.post("/reset")
def reset():
    session["messages"] = [{"role": "system", "content": "Eres un asistente útil y conciso."}]
    session["last_audio"] = None
    session.modified = True
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
