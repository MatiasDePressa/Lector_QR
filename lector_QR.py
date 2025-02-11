import numpy as np
import cv2
from pyzbar.pyzbar import decode
import json

def toma_guardar_foto(nombre_archivo):
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    cv2.imwrite(nombre_archivo, frame)
    cam.release()

def destruir_img(nombre_archivo):
    try:
        import os
        os.remove(nombre_archivo)
        print(f'Imagen {nombre_archivo} fue eliminada')
    except FileNotFoundError:
        print(f'La imagen {nombre_archivo} no fue encontrada')

def leer_qr_y_guardar_json(imagen):
    img = cv2.imread(imagen)
    codigos_qr = decode(img)

    datos_qr = []

    for codigo in codigos_qr:
        datos = {
            'Datos': codigo.data.decode('utf-8'),
            'Tipo de codificacion': codigo.type,
        }

        puntos = codigo.polygon
        if len(puntos) == 4:
            pts = [(punto.x, punto.y) for punto in puntos]
            datos['Puntos'] = pts
            cv2.polylines(img, [np.array(pts, dtype=int)], isClosed=True, color=(0, 255, 0), thickness=2)

        datos_qr.append(datos)

    datos_txt = ''.join(map(str, datos_qr))
    print(datos_qr)

    # Guardar datos en un archivo JSON
    with open('datos_qr.txt', 'w') as archivo_txt:
        archivo_txt.write(datos_txt)

    cv2.imshow('Lector QR', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

nombre_archivo = "qr.jpg"

toma_guardar_foto(nombre_archivo)
leer_qr_y_guardar_json(nombre_archivo)
destruir_img(nombre_archivo)
