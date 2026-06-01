from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='03_books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

"""
all glob patterns
'**/*.txt' - All .txt files in all subfolders
'*.pdf' - All .pdf files in the root directory
'data/*.csv' - All .csv files in the data/ folder
'**/*' - All files (any type, all folders)
"""

docs = loader.load()

print(len(docs))
print(len(docs[0]))

print(docs[0].page_content)
print(docs[0].metadata)

#
# eg for load and lazy load 

# docs = loader.load()
# for document in docs:
#     print(document.metadata)


# docs = loader.lazy_load()
# for document in docs:
#     print(document.metadata)