import streamlit as st

from src.architectures.resnet import resnet18, resnet50

st.title("ResNet")
st.caption("He et al. — Deep Residual Learning for Image Recognition, 2015")

st.markdown(
    """
    Introduced residual (skip) connections, enabling networks with 100+ layers. Won ILSVRC 2015.

    **Residual block (ResNet-18/34):**
    ```
    x → Conv(3×3) → BN → ReLU → Conv(3×3) → BN → (+x) → ReLU
    ```

    **Bottleneck block (ResNet-50+):**
    ```
    x → Conv(1×1, reduce) → Conv(3×3) → Conv(1×1, expand) → BN → (+x) → ReLU
    ```

    | Model | Block | Stage layers | Params |
    |-------|-------|-------------|--------|
    | ResNet-18 | Basic | [2,2,2,2] | 11M |
    | ResNet-34 | Basic | [3,4,6,3] | 21M |
    | ResNet-50 | Bottleneck | [3,4,6,3] | 25M |
    | ResNet-101 | Bottleneck | [3,4,23,3] | 44M |

    **Key ideas:**
    - Skip connections solve the vanishing gradient / degradation problem
    - Batch normalization after every conv
    - Global average pooling instead of large FC layers
    """
)

st.divider()
st.subheader("Implementation")
st.markdown("Model: `src/architectures/resnet.py` — `resnet18()`, `resnet50()`")
st.info("Implement BasicBlock first, verify parameter count matches torchvision, then add Bottleneck.")

st.divider()
st.subheader("Demo")
st.info("Image classification demo goes here.")
