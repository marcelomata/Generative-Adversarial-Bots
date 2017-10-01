import csv
import requests
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pickle

training_mocha = True



def interact_cleverbot(text_input, cleverbot_state=""):
    api_key = "CC4qruTTaiN1tTMKWM4VYhuuc4w"
    link = "http://www.cleverbot.com/getreply?key={}&input={}&cs={}".format(api_key, text_input, cleverbot_state)
    response = requests.get(link)

    res_json = response.json()  # Just like a Python dictionary
    new_cs = res_json['cs']
    output = res_json['output']
    
    return output, new_cs, res_json


# Initialize a movie chatterbot
movie_chatterbot = ChatBot(
    "Movie",
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database='./movie_database.sqlite3'    
)

mocha = movie_chatterbot  # Giving a friendly-sounding alias

dialogue_list = pickle.load(open('dialogue_lines.p','rb'))


        

if training_mocha:
    mocha.set_trainer(ListTrainer)
    mocha.train(dialogue_list[:250])
    mocha.train(dialogue_list[5000:5250])
    mocha.train(dialogue_list[100000:100250])
    mocha.train(dialogue_list[50000:50250])
    mocha.train(dialogue_list[200000:200250])



mocha.read_only = True
print(mocha.read_only)


# List to store the conversation
conversation_record = []

# Initialize the conversation with cleverbot
cleverbot_response, cleverbot_state,_ = interact_cleverbot("")

print("Cleverbot:", cleverbot_response)
print()

conversation_record.append((1,'cleverbot',cleverbot_response))


for interaction in range(2,101):
    
    mocha_response = mocha.get_response(cleverbot_response).text
    cleverbot_response, _, _ = interact_cleverbot(mocha_response, cleverbot_state)
    
    print("Cleverbot: ", cleverbot_response)
    print("Mocha: ", mocha_response)    
    print()
    
    conversation_record.append((interaction,'cleverbot',cleverbot_response))
    conversation_record.append((interaction,'mocha',mocha_response))    



with open("cleverbot_mocha_interactions.csv",'w',newline='') as csvfile:
    recordwriter = csv.writer(csvfile)
    for record in conversation_record:
        recordwriter.writerow(record)
