import streamlit as st

from src.architectures.lenet5 import LeNet5

st.title("LeNet-5")
st.caption("LeCun et al., 1998 — Gradient-Based Learning Applied to Document Recognition")

st.markdown(
    """
    The architecture that started it all. Designed for handwritten digit recognition (MNIST).

    **Architecture:**
    ```
    Input (1×32×32)
      → Conv(6, 5×5) + tanh → AvgPool(2×2)
      → Conv(16, 5×5) + tanh → AvgPool(2×2)
      → Flatten
      → FC(120) + tanh
      → FC(84) + tanh
      → FC(10) + softmax
    ```

    **Key ideas:**
    - Local receptive fields (sparse connectivity)
    - Shared weights (same filter slides over the whole image)
    - Subsampling / pooling for spatial invariance
    - Originally used tanh (modern versions use ReLU)
    """
)

st.divider()
st.subheader("Implementation")
st.markdown("Model: `src/architectures/lenet5.py` — `LeNet5`")
st.info("Implement the model, then add a training demo on MNIST here.")

st.divider()
st.subheader("Demo")
st.info("Interactive digit classification demo goes here.")
