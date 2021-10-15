import openai
import os

class Conversation:
  def __init__(self, openaiId, fId=000000):
    self.id = fId
  
    openai.api_key = openaiId

    self.fname = f"{fId}.txt"
    if os.path.exists(self.fname):
      pass
    else:
      with open(self.fname, "w") as f:
        f.write("The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: ")
  

  def resetContext(self, clear=False):
    if clear:
      clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
      clearConsole()
    with open(self.fname, "w") as f:
      f.write("The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: ")
  

  def send(self, userInput):
    with open(self.fname, "r") as f:
      context = f.read()
    
    prompt = context + userInput + "\nAI:"

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
      f.write(userInput + "\nAI:" +response["choices"][0]["text"] + "\nHuman: ")

    return "AI:" + response["choices"][0]["text"] + "\n"
  

  def loadContext(self):
    with open(self.fname, "r") as f:
      context = f.readlines()
    for i in range(len(context)-1):
      print(context[i])

  
