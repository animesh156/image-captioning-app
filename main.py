# main.py

import streamlit as st
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import torch
from app.caption_generator import CaptionGenerator

# Set the page config
st.set_page_config(page_title="Image Captioning App", layout="centered")

# Title
st.title("🖼️ Image Captioning App")
st.write("Upload an image and get an AI-generated caption.")

# Load model and processor (caching for speed)
@st.cache_resource
def load_model():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base").to(device)
    captioner = CaptionGenerator(model, processor, device)
    return captioner

captioner = load_model()

# Image uploader
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Generate Caption"):
        with st.spinner("Generating caption..."):
            caption = captioner.generate_caption(image)
        st.success("Caption Generated!")
        st.markdown(f"**📝 Caption:** {caption}")
