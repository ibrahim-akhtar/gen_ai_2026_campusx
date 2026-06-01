from langchain_huggingface import HuggingFaceEmbeddings

# https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2 
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

text = "Delhi is the capital of India"

vector = embedding.embed_query(text)

print(str(vector))

# ### for multiple docs
# documents = [
#     "Delhi is the cpital of India",
#     "Kolkata is the capital of West Bengal",
#     "Paris the capital of France"
# ]

# vector = embedding.embed_query(documents)

# print(str(vector))