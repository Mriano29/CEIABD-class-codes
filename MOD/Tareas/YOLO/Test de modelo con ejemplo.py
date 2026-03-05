import cv2
from ultralytics import YOLO

# Cargar modelo entrenado
model = YOLO("C:/Users/mrian/Documents/GitHub/CEIABD-class-codes/MOD/Tareas/YOLO/yolov8n.pt")

# Cargar imagen
image_path = "C:/Users/mrian/Desktop/elefante.jpg"
results = model(image_path, conf=0.3, iou=0.5)

# Leer imagen
image = cv2.imread(image_path)

for result in results:
    boxes = result.boxes
    names = result.names

    for box in boxes:
        # Coordenadas
        xmin, ymin, xmax, ymax = box.xyxy[0]
        xmin, ymin, xmax, ymax = int(xmin), int(ymin), int(xmax), int(ymax)

        # Clase detectada
        class_id = int(box.cls[0])
        label = names[class_id]

        # Dibujar rectángulo
        cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)

        # Dibujar etiqueta
        cv2.putText(image, label,
                    (xmin, ymin - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,
                    (0, 255, 0),
                    2)

# Mostrar imagen
cv2.imshow("Detección", image)
cv2.waitKey(0)
cv2.destroyAllWindows()