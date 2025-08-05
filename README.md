
# 🖼️ Image Captioning App

Upload an image and get an AI-generated caption using a pre-trained BLIP (Bootstrapped Language-Image Pretraining) model.

## 🚀 Features

- Upload `.jpg`, `.jpeg`, or `.png` image files.
- Generates natural language captions for images using BLIP model.
- Powered by HuggingFace Transformers and Streamlit.
- Responsive and clean UI.

## 🛠️ Tech Stack

- Python
- [Streamlit](https://streamlit.io/)
- [HuggingFace Transformers](https://huggingface.co/transformers/)
- BLIP model (`Salesforce/blip-image-captioning-base`)
- PIL (Python Imaging Library)
- PyTorch

## 📂 Project Structure

```
image-captioning-app/
│
├── app/
│   ├── __init__.py
│   └── caption_generator.py       # Core captioning logic using BLIP model
│
|
│
├── main.py                        # Streamlit app entry point
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation (this file)
```

## 🧪 Setup Instructions

1. **Clone the repo**
```bash
git clone https://github.com/your-username/image-captioning-app.git
cd image-captioning-app
```


2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the app**
```bash
streamlit run main.py
```

## 🖼️ Example Screenshot

<img width="1366" height="566" alt="Screenshot (421)" src="https://github.com/user-attachments/assets/7a03c9a8-232f-4ce4-b6d8-075d29c547a3" />

<img width="1366" height="588" alt="Screenshot (420)" src="https://github.com/user-attachments/assets/4af3501d-9e03-45e1-bcb3-efba3e5debc4" />





## 🔮 Future Improvements

- Support for multiple captioning models
- Add image preprocessing options (resize, crop)
- Download caption as `.txt` or share on social media
- Dockerize for easier deployment

---

Made with ❤️ using Streamlit and HuggingFace
