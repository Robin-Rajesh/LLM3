import streamlit as st
from model_utils import generate_response

st.title("🧠 Foundation vs Domain-Specific Model Comparison")

st.markdown("""
Choose a model and input your question or passage for comparison.
- **DeepSeek-R1**: General-purpose foundation model (GPT-2)
- **BioGPT**: Healthcare-specific model (GPT-2 with biomedical prompt)
- **Legal-BERT**: Legal text summarization (FLAN-T5)
""")

# Input text
input_text = st.text_area("Enter your input:", "What is the treatment for diabetes?", height=150)

# Model selection
selected_models = st.multiselect(
    "Select models to compare",
    ["DeepSeek-R1", "BioGPT", "Legal-BERT"],
    default=["DeepSeek-R1", "BioGPT"]
)

if st.button("Generate Responses"):
    st.write("✅ Button clicked!")
    if not input_text.strip():
        st.warning("Please enter some input text.")
    else:
        for model in selected_models:
            with st.spinner(f"Generating with {model}..."):
                output = generate_response(model, input_text)
                st.subheader(f"🔍 {model} Output:")
                st.success(output)
