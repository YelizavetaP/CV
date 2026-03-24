import streamlit as st

st.title("👁️ Computer Vision Learning Lab")
st.markdown(
    """
    A hands-on journey through computer vision — from pixel math to vision-language models.

    Use the sidebar to navigate between topics.
    """
)

st.markdown("## Curriculum Overview")

topics = [
    ("🖼️ Foundations", "Pixels, color spaces, classical filters, feature descriptors"),
    ("🧠 CNNs", "Core architectures implemented by hand: LeNet → MobileNet"),
    ("📦 Object Detection", "YOLO, R-CNN family, DETR"),
    ("✂️ Segmentation", "UNet, SAM, Mask R-CNN"),
    ("🔀 Transformers in CV", "ViT, DINO, Swin, MAE"),
    ("🌐 Vision-Language Models", "CLIP, BLIP, LLaVA, Florence-2"),
]

for title, desc in topics:
    with st.expander(title):
        st.write(desc)
