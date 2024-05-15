from src.infrastructure.ia.image_transformer import TransformerImageGen


class ImageRecognition:
    def __init__(self, transformer_repo: TransformerImageGen):
        self.transformer_repo = transformer_repo

    def execute(self, img_path:str) -> str:
        images = self.transformer_repo.image_segmentation(img_path)
        images_labels = self.transformer_repo.image_classification(images)
        
        return images_labels
