import os
from GPT3context import Conversation


# A simple example for an ongoing conversation with the AI
def interface(conversation):
  # Get the pre existing converastion in the console
  conversation.loadContext()
  while True:
    userinput = input("Human: ")
    if userinput == "CMDexit":
      break
    elif userinput == "CMDreset":
      conversation.resetContext(clear=True)
      conversation.loadContext()
    else:
      print(conversation.send(userinput))


def main():
  # Initialize the Conversation with your OpenAI API key 
  conversation = Conversation(
  os.environ["OPENAI_AUTH"]
  )
  interface(conversation)


if __name__ == "__main__":
  main()