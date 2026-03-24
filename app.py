import streamlit as st

st.set_page_config(
    page_title="Computer Vision Learning Lab",
    page_icon="👁️",
    layout="wide",
)

pg = st.navigation(
    {
        "": [
            st.Page("pages/home.py", title="Home", icon="👁️", url_path="home"),
        ],
        "Foundations": [
            st.Page("pages/foundations/image_basics.py", title="Image Basics", icon="🖼️", url_path="image-basics"),
            st.Page("pages/foundations/classical_cv.py", title="Classical CV", icon="🔬", url_path="classical-cv"),
        ],
        "CNNs": [
            st.Page("pages/cnns/overview.py", title="Overview", icon="🧠", url_path="cnns"),
            st.Page("pages/cnns/lenet5.py", title="LeNet-5", url_path="lenet5"),
            st.Page("pages/cnns/alexnet.py", title="AlexNet", url_path="alexnet"),
            st.Page("pages/cnns/vgg.py", title="VGG", url_path="vgg"),
            st.Page("pages/cnns/resnet.py", title="ResNet", url_path="resnet"),
            st.Page("pages/cnns/mobilenet.py", title="MobileNet", url_path="mobilenet"),
        ],
        "Object Detection": [
            st.Page("pages/detection/overview.py", title="Overview", icon="📦", url_path="detection"),
        ],
        "Segmentation": [
            st.Page("pages/segmentation/overview.py", title="Overview", icon="✂️", url_path="segmentation"),
        ],
        "Transformers in CV": [
            st.Page("pages/transformers/overview.py", title="Overview", icon="🔀", url_path="transformers"),
        ],
        "Vision-Language Models": [
            st.Page("pages/vlms/overview.py", title="Overview", icon="🌐", url_path="vlms"),
        ],
    }
)

pg.run()
