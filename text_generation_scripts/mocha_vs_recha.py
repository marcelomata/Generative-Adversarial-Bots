import csv
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
import pickle

training_mocha = True
training_recha = False


# Initialize a movie chatterbot
movie_chatterbot = ChatBot(
    "Movie",
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database='./movie_database.sqlite3'    
)

mocha = movie_chatterbot  # Giving a friendly-sounding alias


if training_mocha:
    dialogue_list = pickle.load(open('dialogue_lines.p','rb'))
    mocha.set_trainer(ListTrainer)
    mocha.train(dialogue_list[:250])
    mocha.train(dialogue_list[5000:5250])
    mocha.train(dialogue_list[100000:100250])
    mocha.train(dialogue_list[50000:50250])
    mocha.train(dialogue_list[200000:200250])


mocha.read_only = True
print(mocha.read_only)


# read only version of vanilla chatterbot
read_only_vanilla_chatterbot = ChatBot(
    "Read-Only Vanilla",
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
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
mocha_response = ""
cleverbot_state = ""


for interaction in range(1,101):
    recha_response = recha.get_response(mocha_response).text
    mocha_response = mocha.get_response(recha_response).text
    
    print("Recha: ", recha_response)
    print("Mocha: ", mocha_response)    
    print()
    
    conversation_record.append((interaction,'recha',recha_response))
    conversation_record.append((interaction,'mocha',mocha_response))    



with open("cleverbot_mocha_interactions.csv",'w',newline='') as csvfile:
    recordwriter = csv.writer(csvfile)
    for record in conversation_record:
        recordwriter.writerow(record)
