import math

print("palabra Clave 1, ADAPTA");
print("palabra Clave 2, SISTEMAS");
print("palabra Clave 3, DIGITALES");

# miVariable = 10;
# miVariable = miVariable + 5;
# print("El valor de mi variable es",miVariable);
# pi=math.pi;
# print("El valor de pi es",pi);

# radio=10;
# area=pi*radio**2;
# print(f"El area para un circulo de {radio} cm es de {area} cm^2");

# planetas=["Mercurio","Venus","Tierra","Marte","Jupiter","Saturno","Urano","Neptuno"];
# print(planetas[-1]);

# import matplotlib.pyplot as plt

# x = [-5,-4,-3,-2,-1,0,1,2,3,4,5]
# y = 1
# fx = [] #lista vacía

# for elemento in x:
#     fx.append(elemento**3 + y)

# print(f"F(x) = {fx}")

# plt.plot(x,fx)
# plt.style.use("ggplot")
# plt.plot(
#     x, # primero el eje X
#     fx, # luego el eje Y
#     )

# plt.show();

# import numpy as np
# import pandas as pd

# import os
# import warnings
# import random

# import matplotlib.pyplot as plt
# from matplotlib import gridspec

# from sklearn.model_selection import train_test_split

# import tensorflow as tf
# from tensorflow import keras

# import tensorflow as tf

# plt.rc('figure', autolayout=True)
# plt.rc('axes', labelweight='bold', labelsize='large',
#        titleweight='bold', titlesize=18, titlepad=10)
# plt.rc('image', cmap='magma')
# warnings.filterwarnings("ignore")

# drive_test = "https://drive.google.com/file/d/1hBoK0ONDI05BKZi3uO9S3Q6v-H0O9NsU/view?usp=sharing"
# drive_train = "https://drive.google.com/file/d/1r7xj5Rq2Vtl_TDTgiDsgahM8-pJrk5w3/view?usp=sharing"

# ruta_test = 'https://drive.google.com/uc?export=download&id='+drive_test.split('/')[-2]
# ruta_train = 'https://drive.google.com/uc?export=download&id='+drive_train.split('/')[-2]

# test = pd.read_csv(ruta_test)
# train = pd.read_csv(ruta_train)
# train2 = train.drop('label',axis=1)
# labels = train.pop('label')
# # De paso, vemos qué tienen
# train2.head()

# import cv2
# import cv2.text
# import mediapipe as mp
# from math import dist
# import time

# mpHands=mp.solutions.hands
# hands=mpHands.Hands(max_num_hands=1,min_detection_confidence=0.7,min_tracking_confidence=0.7);

# mpDraw=mp.solutions.drawing_utils

# dedos={
#     "indice":[6,8],"anular":[10,12],"mayor":[14,16],"menique":[18,20]
# }

# def coord_x(marcador):
#     return float(str(results.multi_hand_landmarks[-1].landmark[int(marcador)]).split("\n")[0].split(" ")[1])
# def coord_y(marcador):
#     return float(str(results.multi_hand_landmarks[-1].landmark[int(marcador)]).split("\n")[1].split(" ")[1])


# def detectarDedo():
#     if results.multi_hand_landmarks is not None:
#         try:
#             x_palma=coord_x(0);
#             y_palma=coord_y(0);
#             cerrados=[]
#             for medio,punta in dedos.values():
#                 x_medio=coord_x(medio);
#                 y_medio=coord_y(medio);
#                 x_punta=coord_x(punta);
#                 y_punta=coord_y(punta);
#                 d_medio=dist((x_palma,y_palma),(x_medio,y_medio));
#                 d_punta=dist((x_palma,y_palma),(x_punta,y_punta));
#                 if d_medio<d_punta:
#                     cerrados.append(1);
#                 else:
#                     cerrados.append(0);
#             return cerrados;
#         except:pass

# cap = cv2.VideoCapture(0)

# if not cap.isOpened():
#     print("Error al abrir la cámara")
#     exit()

# while True:
#     ret, frame = cap.read()
#     if not ret:
#      print("Error al recibir el frame")
#      break  #

# imgRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
# results=hands.process(imgRGB)
# if results.multi_hand_landmarks:
#     for handLms in results.multi_hand_landmarks:
#         for id,lm in enumerate(handLms.landmark):
#             h,w,c=frame.shape
#             cx,cy=int(lm.x*w),int(lm.y*h)
#             d=[8,12,16,20]
#             deteccion=detectarDedo()
#             if id in d:
#                 if deteccion[d.index(id)]==1:
#                     print(id)
#                     cv2.circle(frame,(cx,cy),10,(0,255,0),-1)#dedo arriba verde
#                 else:
#                     cv2.circle(frame,(cx,cy),10,(0,0,255),-1)#dedo abajo rojo
#         mpDraw.draw_landmarks(frame,handLms,mpHands.HAND_CONNECTIONS)


# deteccion=detectarDedo()

# if deteccion is not None:
#     print(deteccion)
#     cv2.putText(frame,f"dedos detectados={sum(deteccion)}",(20,30),fontFace=0,fontScale=1,color=(0,0,255),thickness=2)

# cv2.imshow("Deteccion de Mano", frame)
# time.sleep(1/30)

# if cv2.waitKey(1) & 0xFF == ord('q'):


# cap.release()
# cv2.destroyAllWindows()

import cv2
import mediapipe as mp
from math import dist

# Inicializar MediaPipe Hands
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=2, min_detection_confidence=0.7, min_tracking_confidence=0.7)
mpDraw = mp.solutions.drawing_utils

# Diccionario con los índices de los dedos (ahora incluye el pulgar)
dedos = {
    "pulgar": [2, 4], "indice": [6, 8], "mayor": [10, 12], "anular": [14, 16], "menique": [18, 20]
}

def coord_x(results, hand_index, marcador):
    return results.multi_hand_landmarks[hand_index].landmark[marcador].x

def coord_y(results, hand_index, marcador):
    return results.multi_hand_landmarks[hand_index].landmark[marcador].y

def detectarDedo(results, hand_index):
    x_palma = coord_x(results, hand_index, 0)
    y_palma = coord_y(results, hand_index, 0)
    cerrados = []

    for nombre, (medio, punta) in dedos.items():
        x_medio, y_medio = coord_x(results, hand_index, medio), coord_y(results, hand_index, medio)
        x_punta, y_punta = coord_x(results, hand_index, punta), coord_y(results, hand_index, punta)

        # Para el pulgar, usamos la distancia en X
        if nombre == "pulgar":
            d_medio = abs(x_palma - x_medio)
            d_punta = abs(x_palma - x_punta)
        else:
            d_medio = dist((x_palma, y_palma), (x_medio, y_medio))
            d_punta = dist((x_palma, y_palma), (x_punta, y_punta))

        if d_medio < d_punta:
            cerrados.append(1)  # Dedo abierto (verde)
        else:
            cerrados.append(0)  # Dedo cerrado (rojo)

    return cerrados

# Capturar video desde la cámara
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error al abrir la cámara")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error al recibir el frame")
        break

    # Convertir a RGB para MediaPipe
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    total_dedos = 0  # Contador para los dedos abiertos

    if results.multi_hand_landmarks:
        for hand_index, hand_landmarks in enumerate(results.multi_hand_landmarks):
            # Detectar los puntos de cada mano individualmente
            deteccion = detectarDedo(results, hand_index)
            for id, lm in enumerate(hand_landmarks.landmark):
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                d = [4, 8, 12, 16, 20]  # Ahora incluye el pulgar (4)

                if id in d:
                    color = (0, 255, 0) if deteccion[d.index(id)] == 1 else (0, 0, 255)
                    cv2.circle(frame, (cx, cy), 10, color, -1)

            # Sumar los dedos abiertos
            total_dedos += sum(deteccion)

            mpDraw.draw_landmarks(frame, hand_landmarks, mpHands.HAND_CONNECTIONS)

        # Mostrar cantidad de dedos detectados
        cv2.putText(frame, f"Dedos detectados: {total_dedos}", (20, 30), fontFace=0, fontScale=1, color=(0, 0, 255), thickness=2)

    # cv2.imshow("Detección de Manos", frame)

    # # Salir con 'q'
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar las caras en la imagen
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Dibujar un rectángulo alrededor de las caras detectadas
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Región de interés (ROI) donde se buscarán los ojos dentro de la cara detectada
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        # Detectar los ojos dentro de la cara
        eyes = eye_cascade.detectMultiScale(roi_gray)

        # Dibujar un rectángulo alrededor de los ojos detectados
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    cv2.imshow('Detección de Ojos', frame)

    # Salir con 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



