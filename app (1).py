
import streamlit as st
import torch

from transformers import (
    BertTokenizer,
    BertForSequenceClassification
)

# =========================
# LOAD MODEL
# =========================

model = BertForSequenceClassification.from_pretrained(
    "bert_news_classifier"
)

tokenizer = BertTokenizer.from_pretrained(
    "bert_news_classifier"
)

model.eval()

# =========================
# LABELS
# =========================

label_names = {
    0: "World",
    1: "Sports",
    2: "Business",
    3: "Science/Technology"
}

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="BERT News Classifier",
    page_icon="📰",
    layout="centered"
)

st.title("📰 BERT News Topic Classifier")

st.markdown(
    "Classify news headlines using a fine-tuned BERT Transformer model."
)

# =========================
# USER INPUT
# =========================

news_text = st.text_area(
    "Enter News Headline"
)

# =========================
# PREDICTION
# =========================

if st.button("Classify News"):

    if news_text.strip() != "":

        inputs = tokenizer(
            news_text,
            return_tensors="pt",
            truncation=True,
            padding=True,
            max_length=128
        )

        with torch.no_grad():

            outputs = model(**inputs)

        prediction = torch.argmax(
            outputs.logits,
            dim=1
        ).item()

        st.success(
            f"Predicted Category: {label_names[prediction]}"
        )

    else:

        st.warning("Please enter news text.")
