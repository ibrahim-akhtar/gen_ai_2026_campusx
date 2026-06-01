from langchain.text_splitter import CharacterTextSplitter

text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis sed nunc suscipit, vehicula mauris nec, mollis enim. Nullam fermentum id magna sed venenatis. Sed ultrices eu massa at consectetur. Aliquam erat volutpat. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Etiam efficitur nec dolor et aliquam. Duis ornare risus sit amet tortor porta, in accumsan odio pellentesque. Duis id velit porta, gravida ipsum non, pulvinar lacus. Aliquam erat volutpat. Vestibulum ut arcu non eros suscipit interdum. Praesent gravida suscipit nisl eget efficitur. Mauris quis metus et erat aliquam lobortis in eu nibh. Ut tincidunt porta laoreet. Vestibulum mattis lobortis ex ut dignissim. Aenean suscipit vulputate massa. Fusce hendrerit et felis et vehicula.

Ut ut ultrices massa. Praesent sollicitudin ligula mauris, quis iaculis turpis pulvinar vitae. Morbi sem dolor, volutpat in pretium non, maximus non sapien. Integer id neque id dui bibendum imperdiet.
"""

splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=''
)

result = splitter.split_text(text)

print(result)