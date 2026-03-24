# Computer Vision Learning Plan

A structured path from image fundamentals to modern vision-language models,
tied to the pages in this Streamlit app.

---

## Primary Resources

### 1. DeepLearning.AI — Deep Learning Specialization (CV part)
https://learn.deeplearning.ai/specializations/deep-learning/information

Relevant courses:
- **Course 4 — Convolutional Neural Networks**
  - Week 1: CNN foundations (convolution, pooling, padding)
  - Week 2: Classic networks (LeNet, AlexNet, VGG, ResNet, Inception)
  - Week 3: Object detection (YOLO, anchor boxes, NMS)
  - Week 4: Face recognition & neural style transfer

### 2. HuggingFace Computer Vision Course
https://huggingface.co/learn/computer-vision-course/unit0/welcome/welcome

Units:
- Unit 1: Fundamentals (image data, OpenCV, augmentations)
- Unit 2: CNNs
- Unit 3: Vision Transformers (ViT, Swin)
- Unit 4: Multimodal models (CLIP, VQA)
- Unit 5: Generative models (VAE, diffusion)
- Unit 6: Video & 3D vision
- Unit 7: Fine-tuning & practical tips

---

## Curriculum by App Page

| Page | Topics | Primary Resource |
|------|--------|-----------------|
| 01 Image Basics | Pixels, color spaces, histograms, I/O | HF Unit 1 |
| 02 Classical CV | Filters, edges, features (SIFT, HOG, ORB) | HF Unit 1 + OpenCV docs |
| 03 CNNs | Layers, architectures, transfer learning | DL.AI Course 4 Wk 1-2 + HF Unit 2 |
| 04 Object Detection | YOLO, R-CNN family, DETR | DL.AI Course 4 Wk 3 + HF Unit 2 |
| 05 Segmentation | UNet, SAM, Mask R-CNN | HF Unit 2-3 |
| 06 Transformers in CV | ViT, DINO, Swin, MAE | HF Unit 3 |
| 07 VLMs | CLIP, BLIP, LLaVA, Florence-2 | HF Unit 4 |

---

## Recommended Additions

### Papers worth reading (roughly in order)
- **LeNet-5** — LeCun et al. 1998 — the original CNN
- **AlexNet** — Krizhevsky et al. 2012 — ImageNet moment
- **ResNet** — He et al. 2015 — residual connections
- **UNet** — Ronneberger et al. 2015 — encoder-decoder segmentation
- **Faster R-CNN** — Ren et al. 2015 — region proposal network
- **YOLOv1** — Redmon et al. 2016 — one-stage detection
- **ViT** — Dosovitskiy et al. 2020 — pure transformer for images
- **CLIP** — Radford et al. 2021 — contrastive image-text pretraining
- **DINO** — Caron et al. 2021 — self-supervised ViT
- **SAM** — Kirillov et al. 2023 — segment anything
- **LLaVA** — Liu et al. 2023 — visual instruction tuning

### Supplementary courses / tutorials
- **fast.ai Practical Deep Learning** (https://course.fast.ai) — very hands-on,
  great for getting models running quickly
- **CS231n Stanford** (https://cs231n.stanford.edu) — rigorous lecture notes +
  assignments; best theoretical grounding for CNNs
- **PyImageSearch** (https://pyimagesearch.com) — practical OpenCV recipes,
  good for classical CV and deployment
- **Roboflow Blog** — practical object detection tutorials, dataset tips, YOLO
  fine-tuning walkthroughs

### Useful datasets to experiment with
- **MNIST / CIFAR-10** — classification warm-up (via `torchvision.datasets`)
- **Pascal VOC / COCO** — object detection & segmentation benchmarks
- **Oxford Pets / Flowers** — fine-tuning classification
- **Roboflow Universe** (https://universe.roboflow.com) — thousands of
  domain-specific datasets, easy export to YOLO format
- **SA-1B** — SAM's 1B-mask dataset for segmentation research

### Tools & libraries to get familiar with
- `albumentations` — fast, rich augmentation pipeline
- `supervision` — annotation & visualization on top of any detector
- `gradio` — quick model demos (complements or replaces Streamlit for model UIs)
- `wandb` / `tensorboard` — experiment tracking
- `label-studio` — open-source annotation tool

---

## Milestone Checklist

- [ ] Run a basic OpenCV pipeline (load → transform → display) in page 01
- [ ] Implement Canny edge detection with interactive sliders in page 02
- [ ] Train a simple CNN on CIFAR-10 from scratch (page 03)
- [ ] Fine-tune a ResNet on a custom dataset (page 03)
- [ ] Run YOLOv8 inference on an uploaded image (page 04)
- [ ] Run SAM on a custom image (page 05)
- [ ] Visualize ViT attention maps (page 06)
- [ ] Build a CLIP-based image search demo (page 07)
- [ ] Build a VQA demo with a small VLM (page 07)
