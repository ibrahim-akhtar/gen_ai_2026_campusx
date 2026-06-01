from langchain_openai import OpenAI

from dotenv import load_dotenv
# what it does?
# from the .env file will load the secret keys to the current file

load_dotenv() # open ai key load/invoked

llm = OpenAI(model='gpt-3.5-turbo-instruct')

# llm.invoke()
# through this method we will communicate with this model

result = llm.invoke("What is the capital of India?")

print(result)