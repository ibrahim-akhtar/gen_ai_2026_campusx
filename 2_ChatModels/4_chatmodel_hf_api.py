# running the model through hugging face api 

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
# import os

load_dotenv()

# model used: https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0 
llm = HuggingFaceEndpoint(
    repo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task = "text-generation"
)
# llm = HuggingFaceEndpoint(
#     model="HuggingFaceH4/zephyr-7b-beta",
#     task="text-generation",
#     huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
# )

chatModel = ChatHuggingFace(llm=llm)

result = chatModel.invoke("What is the capital of India?")

print(result.content)