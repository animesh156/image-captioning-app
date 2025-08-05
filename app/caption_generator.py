# app/caption_generator.py

from PIL import Image
import torch

class CaptionGenerator:
    def __init__(self, model, processor, device):
        self.model = model
        self.processor = processor
        self.device = device

    def generate_caption(self, image: Image.Image) -> str:
        inputs = self.processor(images=image, return_tensors="pt").to(self.device)

        with torch.no_grad():
            output = self.model.generate(**inputs)

        caption = self.processor.decode(output[0], skip_special_tokens=True)
        return caption
