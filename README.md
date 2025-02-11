# Lector de Códigos QR en Python

Este proyecto es un lector de códigos QR que utiliza la cámara para capturar una imagen, leer el código QR contenido en ella y guardar la información en un archivo JSON.

## Requisitos

Para ejecutar este programa, necesitas tener instaladas las siguientes dependencias:

- Python 3.x
- OpenCV (`cv2`)
- NumPy (`numpy`)
- Pyzbar (`pyzbar`)

Puedes instalarlas con el siguiente comando:

```bash
pip install opencv-python numpy pyzbar
```

## Uso

1. Ejecuta el script `lector_QR.py` en tu terminal o entorno de desarrollo.
2. El programa activará la cámara y tomará una foto.
3. Si hay un código QR en la imagen, lo decodificará y extraerá la información.
4. Los datos extraídos se guardarán en un archivo `datos_qr.txt`.
5. La imagen tomada será eliminada automáticamente después de su procesamiento.
6. Se mostrará la imagen con el código QR resaltado.

## Explicación del Código

El script realiza los siguientes pasos:

1. **Captura de imagen:**
   - Usa OpenCV para activar la cámara y tomar una foto.
2. **Lectura del código QR:**
   - Usa `pyzbar` para decodificar el código QR.
   - Extrae la información del código, incluyendo su contenido y tipo de codificación.
   - Dibuja un rectángulo alrededor del código QR detectado.
3. **Guardado de datos:**
   - Los datos extraídos se guardan en `datos_qr.txt` en formato JSON.
4. **Limpieza:**
   - La imagen capturada se elimina después del procesamiento.
5. **Visualización:**
   - La imagen con el código QR resaltado se muestra en una ventana emergente.

## Archivos Generados

- `qr.jpg`: Imagen capturada (se elimina después de la ejecución).
- `datos_qr.txt`: Archivo con la información del código QR detectado.

## Mejoras Posibles

- Guardar los datos en un archivo JSON en lugar de un `.txt`.
- Manejo de múltiples códigos QR en una sola imagen.
- Agregar una interfaz gráfica para facilitar el uso.
- Implementar un modo continuo para escanear varios códigos QR sin reiniciar el script.

## Autor

Desarrollado por Matias De Pressa

