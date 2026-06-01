# ref: https://docs.langchain.com/oss/python/langchain/overview 

from langchain_community.document_loaders import TextLoader

loader = TextLoader('01_cricket.txt', encoding='utf-8')

docs = loader.load()

print(type(docs))
print(len(docs))
print(docs)
print(docs[0])
print(type(docs[0]))

print(docs[0].page_content)
print(docs[0].metadata)

from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

prompt = PrimptTemplate(
    template='Write a summary for the following Poem.\n{poem}'
    input_varibales=['poem']
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke('poem':docs[0].page_content)

print(result)