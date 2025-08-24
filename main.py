from Agents.System_prompt_gen import sys_prompt
from Agents.prompt_engineering import prompt_engn

class interaction:
    def __init__(self):
       pass
    def decision(self):
        give = input("what do you want 'system prompt' or 'prompt engineering'\n").lower().strip()
        if give == 'system prompt':
            user_prompt = input("Enter your prompt: ")
            get = sys_prompt(user_prompt)
            print(get.generate_system_prompt())
        elif give == 'prompt engineering':
            user_prompt = input("Enter your prompt: ")
            get = prompt_engn(user_prompt)
            print(get.generate_prompt())
        else:
            print("Invalid input")
            
if __name__ == "__main__":
    interaction().decision()