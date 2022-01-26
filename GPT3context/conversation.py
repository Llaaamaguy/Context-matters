__author__ = "Llaaamaguy"

import openai
import os


class Conversation(object):
    def __init__(self, openai_id, f_id=000000):
        self.id = f_id

        openai.api_key = openai_id

        self.fname = f"{f_id}.txt"

        self.engine = 'davinci'
        self.temperature = 0
        self.max_tokens = 300
        self.top_p = 1
        self.frequency_penalty = 0
        self.presence_penalty = 0

        if os.path.exists(self.fname):
            pass
        else:
            with open(self.fname, "w") as f:
                f.write(
                    "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever,"
                    " and very friendly.\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help "
                    "you today?\nHuman: ")

    def reset_context(self, clear=False):
        if clear:
            clear_console = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
            clear_console()
        with open(self.fname, "w") as f:
            f.write(
                "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and "
                "very friendly.\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you "
                "today?\nHuman: ")

    def send(self, user_input):
        with open(self.fname, "r") as f:
            context = f.read()

        prompt = context + user_input + "\nAI:"

        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            temperature=0.8,
            max_tokens=300,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            stop=["\n", " Human:", " AI:"]
        )

        with open(self.fname, "a") as f:
            f.write(user_input + "\nAI:" + response["choices"][0]["text"] + "\nHuman: ")

        return "AI:" + response["choices"][0]["text"] + "\n"

    def load_context(self):
        with open(self.fname, "r") as f:
            context = f.readlines()
        for i in range(len(context) - 1):
            print(context[i])

    def ai_settings(self, engine="", temperature=0, max_tokens=300, top_p=1, frequency_penalty=0, presence_penalty=0):
        self.engine = engine
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.top_p = top_p
        self.frequency_penalty = frequency_penalty
        self.presence_penalty = presence_penalty
