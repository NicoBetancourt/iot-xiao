# Use cases package
from src.services.image.image_recognition import ImageRecognition

# Repos
from src.infrastructure.ia.transformer_gen import TransformerGen

_image_repo = TransformerGen()

# Use cases
image_recognition = ImageRecognition(_image_repo).execute