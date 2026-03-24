"""Shared image helpers used across pages."""
import numpy as np
from PIL import Image


def pil_to_numpy(img: Image.Image) -> np.ndarray:
    return np.array(img)


def numpy_to_pil(arr: np.ndarray) -> Image.Image:
    return Image.fromarray(arr.astype(np.uint8))


def load_uploaded_image(uploaded_file) -> np.ndarray:
    """Load a Streamlit UploadedFile as an RGB numpy array."""
    img = Image.open(uploaded_file).convert("RGB")
    return pil_to_numpy(img)
