from ultralytics import YOLO

# Ruta al modelo entrenado con african wildlife
pesos_yolo = "C:/Users/mrian/Documents/GitHub/CEIABD-class-codes/yolov8n.pt" 

# Cargar modelo
model = YOLO(pesos_yolo)

try:
    # Detección con webcam
    results = model.track(
    source=0,
    conf=0.3,
    iou=0.5,
    show=True,
)

except Exception as e:
    print("Ocurrió un error al realizar la detección de objetos:", e)
