from src.infrastructure.ia.transformer_gen import TransformerGen


class ImageRecognition:
    def __init__(self, transformer_repo: TransformerGen):
        self.transformer_repo = transformer_repo

    def execute(self, img_path:str) -> str:
        res = self.transformer_repo.image_recognize(img_path)
        return res
