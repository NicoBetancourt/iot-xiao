# Use cases package
from src.services.image.image_recognition import ImageRecognition

# Repos
from src.infrastructure.ia.image_transformer import TransformerImageGen

_image_repo = TransformerImageGen()

# Use cases
image_list = ImageRecognition(_image_repo).execute