# to view how StrOutputParser + chains works

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# for open ai
# from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

# for open ai wont need the following llm code
llm = HuggingFaceEndpoint(
    repo_id = "TinyLlama/TinyLlama-1.18-Chat-v01.0",
    # repo_id = "google/gamma-2-2b-it",
    task = "text-generation"
)

model = ChatHuggingFace(llm=llm)
# for open ai
# model = ChatOpenAI()


# task:
# 1. give topic to LLM
# 2. LLM response - detailed report
# 3. detailed report - given to LLM
# 4. LLM summarizes report in 5 lines

# 1st prompt -> detailed report
template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

# 2nd prompt -> summary
template2 = PromptTemplate(
    template='Write a 5 line summary on the following text. /n{text}',
    input_variables=['text']
)

parser = StrOutputParser()

chain = template1 | model | parser | template2| model | parser

result = chain.invoke({'topic':'black hole'})

print(result)