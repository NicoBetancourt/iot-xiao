from src.infrastructure.ia.image_transformer import TransformerImageGen


class ImageRecognition:
    def __init__(self, transformer_repo: TransformerImageGen):
        self.transformer_repo = transformer_repo

    def execute(self, img) -> str:
        raw, processed = self.transformer_repo.descrive(img)
        
        return raw, processed
