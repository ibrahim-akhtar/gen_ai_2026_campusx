from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

# dynamic prompt
from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv()
model = ChatOpenAI()

st.header('Research Tool')



paper_input = st.selectbox("Select Research Paper Name", ["Attention is All You Need", "BERT: Pre-Training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"])

style_input = st.selectbox("Select Explanation Style", ["Begineer-Friendly", "Technical", "Code-Oriented", "Mathematical"])

length_input = st.selectbox("Selct Explanation Length", ["Short(1-2 Paragraphs)", "Medium(3-5 Paragraphs)", "Long(Detailed Explanation)"])

# template
template = load_prompt('02_generated_template.json')

# fill the place holders
prompt = template.invoke({
    'paper_input':paper_input,
    'style_input':style_input,
    'length_input':length_input
})

if st.button('Summarize'):
    result = model.invoke(prompt)
    st.write(result.content)