# Computer Vision Learning Lab

Hands-on CV journey from image basics to vision-language models, presented as an interactive Streamlit app.

## Structure

```
app.py                  # Home page
pages/
  01_image_basics.py
  02_classical_cv.py
  03_cnns.py
  04_object_detection.py
  05_segmentation.py
  06_transformers_cv.py
  07_vlms.py
utils/
  image_utils.py        # Shared helpers
experiments/            # Scratch notebooks / scripts
assets/
  sample_images/
LEARNING_PLAN.md        # Curriculum, resources, milestones
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```bash
streamlit run app.py
```

## Resources

See [LEARNING_PLAN.md](LEARNING_PLAN.md) for the full curriculum and recommended reading.
