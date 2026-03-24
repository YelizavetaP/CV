import streamlit as st

from src.architectures.alexnet import AlexNet

st.title("AlexNet")
st.caption("Krizhevsky, Sutskever, Hinton — ImageNet Classification with Deep CNNs, 2012")

st.markdown(
    """
    Won ILSVRC 2012 by a large margin and kicked off the deep learning era in CV.

    **Architecture:**
    ```
    Input (3×224×224)
      → Conv(96, 11×11, s=4) + ReLU → MaxPool(3×3, s=2)
      → Conv(256, 5×5, pad=2) + ReLU → MaxPool(3×3, s=2)
      → Conv(384, 3×3, pad=1) + ReLU
      → Conv(384, 3×3, pad=1) + ReLU
      → Conv(256, 3×3, pad=1) + ReLU → MaxPool(3×3, s=2)
      → Flatten
      → FC(4096) + ReLU + Dropout(0.5)
      → FC(4096) + ReLU + Dropout(0.5)
      → FC(1000) + softmax
    ```

    **Key ideas introduced:**
    - ReLU activations (faster training than tanh/sigmoid)
    - Dropout for regularization
    - Data augmentation (flips, crops, color jitter)
    - Originally trained on 2 GPUs in parallel
    """
)

st.divider()
st.subheader("Implementation")
st.markdown("Model: `src/architectures/alexnet.py` — `AlexNet`")
st.info("Implement the model, then add a training demo on CIFAR-10 here.")

st.divider()
st.subheader("Demo")
st.info("Image classification demo goes here.")
