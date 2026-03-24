import streamlit as st

st.title("🧠 CNNs — Overview")
st.markdown(
    """
    This section covers convolutional neural networks from first principles,
    then implements key architectures by hand in PyTorch.

    **Core concepts to understand before the architectures:**
    - Convolution operation & learnable filters
    - Padding, stride, receptive field
    - Pooling (max, average, global)
    - Batch normalization & dropout
    - Transfer learning & fine-tuning

    **Architectures covered:**
    | Model | Year | Key idea |
    |-------|------|----------|
    | LeNet-5 | 1998 | First practical CNN |
    | AlexNet | 2012 | Deep CNN + ReLU + dropout |
    | VGG | 2014 | Depth via uniform 3×3 convs |
    | ResNet | 2015 | Residual / skip connections |
    | MobileNet | 2017 | Depthwise separable convolutions |
    | EfficientNet | 2019 | Compound scaling |

    Navigate the sidebar to explore each one.
    """
)
