

import csv
import requests
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


training_recha = False



def interact_cleverbot(text_input, cleverbot_state=""):
    api_key = "CC4qruTTaiN1tTMKWM4VYhuuc4w"
    link = "http://www.cleverbot.com/getreply?key={}&input={}&cs={}".format(api_key, text_input, cleverbot_state)
    response = requests.get(link)

    res_json = response.json()  # Just like a Python dictionary
    new_cs = res_json['cs']
    output = res_json['output']
    
    return output, new_cs, res_json



# read only version of vanilla chatterbot
read_only_vanilla_chatterbot = ChatBot(
    "Read-Only Vanilla",
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        "chatterbot.logic.MathematicalEvaluation",
        "chatterbot.logic.TimeLogicAdapter",
        "chatterbot.logic.BestMatch"
    ],
    database='./read_only_vanilla_database.sqlite3'
)

recha = read_only_vanilla_chatterbot

if training_recha:
    # Training Recha
    recha.set_trainer(ChatterBotCorpusTrainer)
    recha.train(
        "chatterbot.corpus.english"
    )


# Locks the bot so we can't edit it anymore
recha.read_only = True
print(recha.read_only)


# List to store the conversation
conversation_record = []


# Initialize the conversation with cleverbot
cleverbot_response, cleverbot_state,res_json = interact_cleverbot("")

print("Cleverbot:", cleverbot_response)
print()

conversation_record.append((1,'cleverbot',cleverbot_response))
recha_response = recha.get_response(cleverbot_response).text

                                 
for interaction in range(2,101):
    recha_response = recha.get_response(cleverbot_response).text
    cleverbot_response, _, _ = interact_cleverbot(recha_response, cleverbot_state)
    
    print("Recha: ", recha_response)
    print("Cleverbot: ", cleverbot_response)
    print()
    
    conversation_record.append((interaction,'recha',recha_response))
    conversation_record.append((interaction,'cleverbot',cleverbot_response))


with open("cleverbot_recha_interaction.csv",'w',newline='') as csvfile:
    recordwriter = csv.writer(csvfile)
    for record in conversation_record:
        recordwriter.writerow(record)





