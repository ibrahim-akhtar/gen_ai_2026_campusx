# for multiple queries

from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

# https://developers.openai.com/api/docs/guides/embeddings 
embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)
# dimension = 32 - very small vector

documents = [
    "Delhi is the cpital of India",
    "Kolkata is the capital of West Bengal",
    "Paris the capital of France"
]

result = embedding.embed_documents(documents)

print(str(result))