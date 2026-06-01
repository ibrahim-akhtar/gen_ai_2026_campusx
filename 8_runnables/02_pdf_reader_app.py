# pdf load
#   |
# splits
#   |
# embeddings
#   |
# vector database
#   |
# retriver
#   |
# LLM
#   |
# parser

from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI

# load the document
loader = TextLoader("docs.txt") # ensure docs.txt exists in the same path
documents = loader.load()

# split the text into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = text_splitter.split_documents(documents)

# convert text into embeddings & store in FAISS
vectorstore = FAISS.from_documents(docs, OpenAIEmbeddings())

# create a retriever (fetches relevant documents)
retriever = vectorstore.as_retriever()

# manually retrieve relevant documents
query = "What are the key takeaways from the document?"
retrieved_docs = retriever.get_relevant_documents(query)

# combine retrieved text into a single prompt
retrived_text = "\n".join([doc.page_content for doc in retrieved_docs])

# initialize the llm
llm = OpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

# manually pass the retrieved text to llm
prompt = f"Based on the following text, answer the question: {query}\n\n{retrived_text}"
answer = llm.predict(prompt)

# print the answer
print("Answer:", answer)