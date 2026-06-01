# to view how result.content works

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# for open ai
# from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

# for open ai wont need the following llm code
llm = HuggingFaceEndpoint(
    repo_id = "TinyLlama/TinyLlama-1.18-Chat-v01.0",
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

prompt1 = template1.invoke({'topic':'black hole'})
result1 = model.invoke(prompt1)

prompt2 = template2.invoke({'text':result1.content})
result2 = model.invoke(prompt2)

print(result2.content)