from ultralytics import YOLO

# Cargar modelo preentrenado YOLOv8n
model = YOLO("yolov8n.pt")

# Entrenar
model.train(
    data="C:/Users/mrian/Documents/GitHub/CEIABD-class-codes/MOD/Tareas/YOLO/dataset/african-wildlife.yaml", 
    epochs=5 ,          # número de épocas
    imgsz=640,          # tamaño de imagen
    batch=16,           # tamaño de batch (ajusta según GPU)
    project="runs/train", 
    name="african_wildlife_yolo",
    exist_ok=True      
)