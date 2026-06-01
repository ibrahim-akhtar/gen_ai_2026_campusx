from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model = ChatOpenAI()

# schema
class Review(TypedDict):
    summary: str
    sentiment: str

structured_model = model.with_structured_output(Review)

result = model.invoke(
    """
    YOUR_REVIEW
    """
)

print(result)
print(result['summary'])
print(result['sentiment'])