from api.prompt import Prompt
import os
from openai import OpenAI
client = OpenAI()

client.api_key = os.getenv("OPENAI_API_KEY")


class ChatGPT:
    def __init__(self):
        self.prompt = Prompt()
        self.model = os.getenv("OPENAI_MODEL", default = "gpt-4-turbo-preview")
        self.temperature = float(os.getenv("OPENAI_TEMPERATURE", default = 0.5))
        self.max_tokens = int(os.getenv("OPENAI_MAX_TOKENS", default = 1000))

    def get_response(self):
        response = client.chat.completions.create(
            model=self.model,
            messages=self.prompt.generate_prompt(),
        )
        return response.choices[0].message.content

    def add_msg(self, text):
        self.prompt.add_msg(text)
