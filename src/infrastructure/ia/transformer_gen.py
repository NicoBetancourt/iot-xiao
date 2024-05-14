# from src.infrastructure.utils.init_generator import generator
from src.main import generator

class TransformerGen:
    def __init__(self):
        self.generator = generator

    def image_recognize(self, img_path):
        return self.generator(img_path, points_per_batch = 256)