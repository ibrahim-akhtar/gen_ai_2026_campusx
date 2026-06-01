# to view how JsonOutputParser + chain works

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# for open ai
# from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser


load_dotenv()

# for open ai wont need the following llm code
llm = HuggingFaceEndpoint(
    repo_id = "TinyLlama/TinyLlama-1.18-Chat-v01.0",
    task = "text-generation"
)

model = ChatHuggingFace(llm=llm)
# for open ai
# model = ChatOpenAI()

parser = JsonOutputParser()

# 1st prompt -> detailed report
template = PromptTemplate(
    template='Give me the name, age, and city of a fictional person \n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({})
# blank dictionary because of no input variables

print(type(result))
print(result)
print(result['name'])