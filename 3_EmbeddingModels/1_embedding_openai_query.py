from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

# https://developers.openai.com/api/docs/guides/embeddings 
embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)
# dimension = 32 - very small vector

result = embedding.embed_query("Delhi is the capital of India")

print(str(result))