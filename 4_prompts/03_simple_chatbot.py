# chatbot - simple
# does not store history

from langchain_openai import ChatOpenAI
from dotenv impoort load_dotenv

load_dotenv()

model = ChatOpenAI()

while True:
    user_input = input('You: ')
    if user_input == 'exit':
        break
    result = model.invoke(user_input)
    print('AI: ',result.content)