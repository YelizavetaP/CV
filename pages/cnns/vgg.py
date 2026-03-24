import streamlit as st

from src.architectures.vgg import VGG

st.title("VGG")
st.caption("Simonyan & Zisserman — Very Deep Convolutional Networks for Large-Scale Image Recognition, 2014")

st.markdown(
    """
    Showed that depth via uniform 3×3 filters is the key driver of performance.

    **Architecture (VGG-16):**
    ```
    Input (3×224×224)
      → [Conv(64, 3×3)] × 2 → MaxPool
      → [Conv(128, 3×3)] × 2 → MaxPool
      → [Conv(256, 3×3)] × 3 → MaxPool
      → [Conv(512, 3×3)] × 3 → MaxPool
      → [Conv(512, 3×3)] × 3 → MaxPool
      → Flatten
      → FC(4096) → FC(4096) → FC(1000)
    ```

    **Key ideas:**
    - Two 3×3 convs = one 5×5 receptive field, but fewer params + more non-linearity
    - Uniform, simple design — easy to understand and modify
    - Large FC layers (138M params total, mostly FC)
    - Excellent feature extractor for transfer learning
    """
)

st.divider()
st.subheader("Implementation")
st.markdown("Model: `src/architectures/vgg.py` — `VGG(variant='vgg16')`")
st.info("Implement the model. Try both VGG-16 and VGG-19 using the CONFIGS dict.")

st.divider()
st.subheader("Demo")
st.info("Image classification demo goes here.")
