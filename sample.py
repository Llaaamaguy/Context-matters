import os
from GPT3context import Conversation


# A simple example for an ongoing conversation with the AI
def interface(conversation):
  # Get the pre existing converastion in the console
  conversation.load_context()
  while True:
    userinput = input("Human: ")
    if userinput == "CMDexit":
      break
    elif userinput == "CMDreset":
      conversation.reset_context(clear=True)
      conversation.load_context()
    else:
      print(conversation.send(userinput))


def main():
  # Initialize the Conversation with your OpenAI API key 
  conversation = Conversation(
  os.environ["OPENAI_AUTH"]
  )
  interface(conversation)

main()
