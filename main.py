import os
from conversation import Conversation


def interface(conversation):
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
  conversation = Conversation(
  os.environ["OPENAI_AUTH"]
  )
  interface(conversation)


if __name__ == "__main__":
  main()