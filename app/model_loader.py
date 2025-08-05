# app/model_loader.py

from transformers import BlipProcessor, BlipForConditionalGeneration
import torch

class ImageCaptioningModel:
    def __init__(self, model_name="Salesforce/blip-image-captioning-base", device=None):
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.processor = BlipProcessor.from_pretrained(model_name)
        self.model = BlipForConditionalGeneration.from_pretrained(model_name).to(self.device)

    def get_model(self):
        return self.model

    def get_processor(self):
        return self.processor

    def get_device(self):
        return self.device
