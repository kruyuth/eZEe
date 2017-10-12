from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
chatbot = ChatBot("PYTHON BOT")
conversation = [
    "สวัสดี",
    "ดีจ้า",
    "ทำไรอยู่",
    "กินข้าว",
    "ลำไย",
    "มะม่วง"
]
chatbot.set_trainer(ListTrainer)
chatbot.train(conversation)
print("\nReady!")
while(True):
  raw = input('me >')
  decoded = str(raw)
  response = chatbot.get_response(decoded)
  print("bot >>",response)
