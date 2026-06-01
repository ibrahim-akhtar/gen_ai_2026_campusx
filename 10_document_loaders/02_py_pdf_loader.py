from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('02_curriculum.pdf')

docs = loader.load()

print(docs)
print(len(docs))

print(docs[0].page_content)
print(docs[0].metadata)

print(type(docs[0]))