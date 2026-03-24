import streamlit as st

from src.architectures.mobilenet import MobileNetV1, MobileNetV2

st.title("MobileNet")
st.caption("Howard et al. — MobileNets: Efficient CNNs for Mobile Vision Applications, 2017")

st.markdown(
    """
    Designed for on-device / real-time inference via **depthwise separable convolutions**.

    **Why it's efficient:**
    ```
    Standard conv (3×3, 32→64):     32 × 64 × 3×3 = 18,432 ops
    Depthwise (3×3, per channel):   32 × 3×3       =    288
    Pointwise (1×1, 32→64):         32 × 64        =  2,048
    Total:                                            2,336  (~8× fewer)
    ```

    **V1 block:**
    ```
    Depthwise Conv(3×3) → BN → ReLU → Pointwise Conv(1×1) → BN → ReLU
    ```

    **V2 inverted residual block:**
    ```
    Pointwise (expand, ReLU6) → Depthwise (ReLU6) → Pointwise (project, linear) → (+x)
    ```

    **Key ideas:**
    - Factorize spatial + channel mixing into separate ops
    - Width multiplier α scales channel count across the whole network
    - V2's linear bottleneck preserves information (no ReLU at projection)
    """
)

st.divider()
st.subheader("Implementation")
st.markdown("Model: `src/architectures/mobilenet.py` — `MobileNetV1`, `MobileNetV2`")
st.info("Implement V1 first (just DepthwiseSeparableConv blocks), then tackle V2's inverted residuals.")

st.divider()
st.subheader("Demo")
st.info("Image classification demo goes here.")
