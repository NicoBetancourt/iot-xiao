from src.infrastructure.utils.init_generator import generator, model, processor
import numpy as np
from urllib.request import urlopen
import cv2

class TransformerImageGen:
    def __init__(self):
        self.generator = generator

    def image_segmentation(self, img_path:str):
        outputs =  self.generator(img_path, points_per_batch = 256)
        raw_image = open_image_from_url(img_path)
        images = []
        # Recorre cada máscara en la lista y muestra el recorte correspondiente de la imagen original
        for mask in outputs['masks']:
            # Aplica la máscara a la imagen original
            recorte = np.copy(raw_image)
            recorte[~mask] = 0  # Establece a cero los píxeles que no están dentro de la máscara

            # Encuentra los límites del recorte
            nonzero_indices = np.nonzero(mask)
            min_y, max_y = np.min(nonzero_indices[0]), np.max(nonzero_indices[0])
            min_x, max_x = np.min(nonzero_indices[1]), np.max(nonzero_indices[1])

            # Realiza el recorte basado en los límites encontrados
            images.append(recorte[min_y:max_y, min_x:max_x])
        return images
    
    
    def image_classification(self, images:list):
        # outputs =  self.generator(img_path, points_per_batch = 256)
        images_labels = {}
        for image in images:
            inputs = processor(images=image, return_tensors="pt")
            outputs = model(**inputs)
            logits = outputs.logits
            # model predicts one of the 1000 ImageNet classes
            predicted_class_idx = logits.argmax(-1).item()
            predicted_label = model.config.id2label[predicted_class_idx]

            if predicted_label in images_labels:
                images_labels[predicted_label] += 1
            else:
                images_labels[predicted_label] = 1
             
        return images_labels
    

def open_image_from_url(url):
    resp = urlopen(url)
    imagen_bytes = np.asarray(bytearray(resp.read()), dtype="uint8")
    # Decodifica la matriz de bytes en una imagen
    imagen = cv2.imdecode(imagen_bytes, cv2.IMREAD_COLOR)
    return imagen