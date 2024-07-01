from src.infrastructure.utils.init_generator import generator, model, processor
import numpy as np
from urllib.request import urlopen
from langchain_community.llms.ollama import Ollama
from src.infrastructure.utils import utils as u
import cv2
from PIL import Image
from io import BytesIO

class TransformerImageGen:

    def __init__(self, model="llava"):
        self.model = Ollama(model=model)

    def descrive(self, contents):
        pil_image = Image.open(BytesIO(contents))
        image_b64 = u.convert_to_base64(pil_image)
        llm_with_image_context = self.model.bind(images=[image_b64])
        response = llm_with_image_context.invoke("could you please create a dictionary with the ingredients of the image and the quantities?")
        ingredients = u.extract_content_between_backticks(response)
        return response, ingredients