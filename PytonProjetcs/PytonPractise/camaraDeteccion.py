import cv2
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error al abrir la cámara")
    exit()
    
while True:
    ret, frame = cap.read()
    if not ret:
     print("Error al recibir el frame")
     break
        
    cv2.imshow("Deteccion", frame)
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
cap.release()
cv2.destroyAllWindows()