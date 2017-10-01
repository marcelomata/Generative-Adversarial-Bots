

import csv
import requests
from chatterbot import ChatBot
from chatterbot.trainers import UbuntuCorpusTrainer


training_ubuncha = True


def interact_cleverbot(text_input, cleverbot_state=""):
    api_key = "CC4qruTTaiN1tTMKWM4VYhuuc4w"
    link = "http://www.cleverbot.com/getreply?key={}&input={}&cs={}".format(api_key, text_input, cleverbot_state)
    response = requests.get(link)

    res_json = response.json()  # Just like a Python dictionary
    new_cs = res_json['cs']
    output = res_json['output']
    
    return output, new_cs, res_json


# ubuntu chatterbot
ubuntu_chatterbot = ChatBot(
    "Ubuntu",
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        "chatterbot.logic.MathematicalEvaluation",
        "chatterbot.logic.TimeLogicAdapter",
        "chatterbot.logic.BestMatch"
    ],
    database='./ubuntu_database.sqlite3'
)

ubuncha = ubuntu_chatterbot

if training_ubuncha:
    # Training ubuncha
    ubuncha.set_trainer(UbuntuCorpusTrainer)
    ubuncha.train()


# Locks the bot so we can't edit it anymore
ubuncha.read_only = True
print(ubuncha.read_only)


# List to store the conversation
conversation_record = []


# Initialize the conversation with cleverbot
cleverbot_response, cleverbot_state,res_json = interact_cleverbot("")

print("Cleverbot:", cleverbot_response)
print()

conversation_record.append((1,'cleverbot',cleverbot_response))
ubuncha_response = ubuncha.get_response(cleverbot_response).text

                                 
for interaction in range(2,101):
    ubuncha_response = ubuncha.get_response(cleverbot_response).text
    cleverbot_response, _, _ = interact_cleverbot(ubuncha_response, cleverbot_state)
    
    print("Ubuncha: ", ubuncha_response)
    print("Cleverbot: ", cleverbot_response)
    print()
    
    conversation_record.append((interaction,'ubuncha',ubuncha_response))
    conversation_record.append((interaction,'cleverbot',cleverbot_response))


with open("cleverbot_ubuncha_interactions.csv",'w',newline='') as csvfile:
    recordwriter = csv.writer(csvfile)
    for record in conversation_record:
        recordwriter.writerow(record)
