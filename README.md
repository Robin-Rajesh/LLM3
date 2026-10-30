# 🧠 Foundation vs Domain-Specific Model Comparison

A Streamlit app that sends the same input to different language models and shows their responses side by side. It illustrates how general-purpose models differ from domain-specific ones in healthcare and legal settings.

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![Hugging Face](https://img.shields.io/badge/Hugging_Face-Transformers-FFD21E)

## 🔍 Models

To keep it lightweight enough to run locally, the app uses smaller stand-in models:

| Option in the app | Represents | Model actually used |
|---|---|---|
| DeepSeek-R1 | General foundation model | `gpt2` |
| BioGPT | Healthcare-specific model | `gpt2` with a medical-assistant prompt |
| Legal-BERT | Legal summarization | `google/flan-t5-base` (summarize prompt) |

The models run on a GPU if one is available.

## 🚀 Getting Started

```bash
pip install -r requirements.txt
streamlit run app.py
```

Enter a question or passage, choose the models to compare, and click **Generate Responses**. The models download from Hugging Face on first run.

## 📂 Files

- `app.py`: Streamlit interface
- `model_utils.py`: model loading and response generation
