from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embeddings = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=300)

documents = [
    "Delhi is the cpital of India",
    "Kolkata is the capital of West Bengal",
    "Paris the capital of France"
]

query = "What is the capital of France"

doc_embeddings = embeddings.embed_documents(documents)
query_embedding = embeddings.embed_query(query)

# print(cosine_similarity([query_embedding], doc_embeddings))

scores = cosine_similarity([query_embedding], doc_embeddings)[0] # 2d lista nd we want a simple list

# print(list(ennumerate(scores)))
# print(sored(list(ennumerate(scores)), key=lambda x:x[1]))
# print(sorted(list(ennumerate(scores)), key=lambda x:x[1])[-1])

index, score = sorted(list(ennumerate(scores)), key=lambda x:x[1])[-1]

print(query)
print(documents[index])
print("Similarity Score:", score)