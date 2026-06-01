from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
model = ChatOpenAI()

st.header('Research Tool')

# # static prompt
# user_input = st.text_input('Enter your Prompt')

# if st.button('Summarize'):
#     result = model.invoke(user_input)
#     st.write(result.content)

# dynamic prompt
from langchain_core.prompts import PromptTemplate

paper_input = st.selectbox("Select Research Paper Name", ["Attention is All You Need", "BERT: Pre-Training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"])

style_input = st.selectbox("Select Explanation Style", ["Begineer-Friendly", "Technical", "Code-Oriented", "Mathematical"])

length_input = st.selectbox("Selct Explanation Length", ["Short(1-2 Paragraphs)", "Medium(3-5 Paragraphs)", "Long(Detailed Explanation)"])

# template
template = PromptTemplate(
    template="""
    Please summarize the research paper titled "{paper_input}" with the following specifications:
    Explanation Style: {style_input}
    Explanation Length: {length_input}
    1. Mathematical Details:
    - Include relevant mathematical equations if present in the paper.
    - Explain the mathematical concepts using simple, intuitive code snippets where applicable.
    2. Analogies:
    - Use relatable analogies to simplify complex ideas.
    If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.
    Ensure the summary is clear, accurate, and aligned with the provided style and length.
    """,
    input_variables=['paper_input', 'style_input','length_input']
)

# fill the place holders
prompt = template.invoke({
    'paper_input':paper_input,
    'style_input':style_input,
    'length_input':length_input
})

if st.button('Summarize'):
    result = model.invoke(prompt)
    st.write(result.content)