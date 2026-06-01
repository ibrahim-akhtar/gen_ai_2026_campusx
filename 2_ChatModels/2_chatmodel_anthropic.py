from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

# https://platform.claude.com/docs/en/home 
chatModel = ChatAnthropic(model="claude-sonnet-4-6")
# can set temperature & max_completion_tokens

result = chatModel.invoke("What is the capital of India?")

print(result.content)