# 📰 BERT News Topic Classifier using Transformers

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![Transformers](https://img.shields.io/badge/HuggingFace-Transformers-yellow?style=for-the-badge)
![PyTorch](https://img.shields.io/badge/PyTorch-DeepLearning-red?style=for-the-badge&logo=pytorch)
![Streamlit](https://img.shields.io/badge/Streamlit-WebApp-ff4b4b?style=for-the-badge&logo=streamlit)
![BERT](https://img.shields.io/badge/BERT-NLP-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Project-Completed-success?style=for-the-badge)

</p>

---

# 📌 Project Overview

This project implements a **Transformer-based News Topic Classification System** using **BERT (Bidirectional Encoder Representations from Transformers)** and the **AG News Dataset**.

The model is fine-tuned using **transfer learning** to classify news headlines into predefined categories:

- 🌍 World
- ⚽ Sports
- 💼 Business
- 💻 Science/Technology

The project demonstrates a complete end-to-end NLP pipeline including:

- Dataset preprocessing
- Tokenization
- Transformer fine-tuning
- Model evaluation
- Real-time inference
- Streamlit deployment

---

# 🎯 Objectives

The primary objectives of this project are:

- Fine-tune a pre-trained BERT model for text classification
- Build a robust NLP classification pipeline
- Evaluate model performance using accuracy and F1-score
- Deploy the model using Streamlit
- Demonstrate practical usage of Transformer architectures

---

# 🧠 Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core Programming Language |
| Hugging Face Transformers | Transformer Model Fine-tuning |
| PyTorch | Deep Learning Framework |
| scikit-learn | Evaluation Metrics |
| Streamlit | Web Deployment |
| Google Colab | Training Environment |
| AG News Dataset | NLP Benchmark Dataset |

---

# 📂 Dataset

The project uses the **AG News Dataset** available from Hugging Face Datasets.

### Dataset Categories

| Label | Category |
|---|---|
| 0 | World |
| 1 | Sports |
| 2 | Business |
| 3 | Science/Technology |

### Dataset Features

- Large-scale news classification dataset
- Balanced category distribution
- Widely used NLP benchmark dataset

---

# 🏗️ Project Architecture

```text
News Headlines
       ↓
Text Tokenization
       ↓
BERT Tokenizer
       ↓
BERT Transformer Model
       ↓
Fine-Tuning
       ↓
Prediction Layer
       ↓
News Category Output
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/maw-khan/bert-news-topic-classifier-transformers.git
```

---

# 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🚀 Running the Project

## Train Model

Run the Jupyter Notebook in Google Colab:

```text
bert_news_classifier.ipynb
```

---

# 🌐 Run Streamlit Application

```bash
streamlit run app.py
```

---

# 🧪 Model Training

The BERT model used:

```text
bert-base-uncased
```

### Training Features

- Transfer Learning
- Transformer Fine-tuning
- GPU Acceleration
- Attention-based Contextual Learning

### Training Configuration

| Parameter | Value |
|---|---|
| Epochs | 2 |
| Batch Size | 16 |
| Learning Rate | 2e-5 |
| Max Length | 128 |
| Optimizer | AdamW |

---

# 📊 Evaluation Metrics

The model is evaluated using:

- Accuracy
- Weighted F1-score
- Classification Report
- Confusion Matrix

### Expected Performance

| Metric | Score |
|---|---|
| Accuracy | 92% - 95% |
| F1 Score | 92% - 95% |

---

# 💻 Streamlit Web Application

The project includes a real-time Streamlit frontend for interactive news classification.

### Features

✅ User-friendly Interface  
✅ Real-time Predictions  
✅ Transformer-based Inference  
✅ Lightweight Deployment  
✅ Clean UI Design

---

# 📁 Project Structure

```text
bert-news-topic-classifier-transformers/
│
├── bert_news_classifier.ipynb
├── app.py
├── requirements.txt
├── README.md
│
├── bert_news_classifier/
│   ├── config.json
│   ├── model.safetensors
│   ├── tokenizer.json
│   ├── tokenizer_config.json
│   
├── screenshots/
    ├── training_results.png
    ├── streamlit_ui.png
    └── prediction_output.png

```

---

# 📌 Sample Prediction

### Input

```text
Apple launches new AI-powered MacBook with advanced neural processing capabilities.
```

### Predicted Output

```text
Science/Technology
```

---

# 📈 Key Learning Outcomes

This project provided hands-on experience in:

- Natural Language Processing (NLP)
- Transformer Architectures
- BERT Fine-tuning
- Text Classification
- Transfer Learning
- Deep Learning Workflows
- Model Deployment
- Streamlit Application Development

---

# 🔥 Future Improvements

Potential future enhancements include:

- Multi-language classification
- DistilBERT optimization
- Model quantization
- Cloud deployment
- Real-time API integration
- Attention visualization
- Explainable AI techniques

---

Focused Areas:

- Transformer Models
- NLP Systems
- Deep Learning
- Model Deployment

---

# 👨‍💻 Author

### Muhammad Ali Waris Khan

---

# 📜 License

This project is developed for educational and internship purposes.

---
