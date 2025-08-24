from groq import Groq
import os
from system_prompt import prompt_sys_gen
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("groq_api")

if api_key is None:
    print("groq_api not found")
    exit(1)

class sys_prompt:
    def __init__(self, user_prompt):
        self.client = Groq(api_key = api_key)
        self.user_prompt = user_prompt
        self.prompt_sys_gen = prompt_sys_gen

    def generate_system_prompt(self):
        response = self.client.chat.completions.create(
            model=os.getenv("MODEL"),
            messages=[
                {"role": "system", "content": self.prompt_sys_gen},
                {"role": "user", "content": self.user_prompt},
            ],
            stream = True
        )

        for chunk in response:
            print(chunk.choices[0].delta.content, end="", flush=True)


    