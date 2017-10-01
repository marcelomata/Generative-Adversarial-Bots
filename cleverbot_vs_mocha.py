import csv
import requests
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

training_mocha = True



def interact_cleverbot(text_input, cleverbot_state=""):
    api_key = "CC4qruTTaiN1tTMKWM4VYhuuc4w"
    link = "http://www.cleverbot.com/getreply?key={}&input={}&cs={}".format(api_key, text_input, cleverbot_state)
    response = requests.get(link)

    res_json = response.json()  # Just like a Python dictionary
    new_cs = res_json['cs']
    output = res_json['output']
    
    return output, new_cs, res_json


with open('movie_lines.txt','r') as file:
    raw_movie_data = file.readlines()

print("Original length of movie data:",len(raw_movie_data))



movie_data = []

for line_raw in raw_movie_data:
    line_list = line_raw.split("\n")[0].split("+++$+++")
    movie_data.append(line_list[3:])


# Here we are removing the repetitions

previous_name = None
line_number = 0

while line_number < len(movie_data):
    current_name, dialogue = movie_data[line_number]
    
    if current_name == previous_name:
        movie_data[line_number-1][1] += "\n" + movie_data.pop(line_number)[1]
        line_number -= 1
                
    previous_name = current_name
    line_number += 1

print("New length of data:",len(movie_data))

dialogue_list = [line[1] for line in movie_data]



# Initialize a movie chatterbot
movie_chatterbot = ChatBot(
    "Movie",
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        "chatterbot.logic.MathematicalEvaluation",
        "chatterbot.logic.TimeLogicAdapter",
        "chatterbot.logic.BestMatch"
    ],
    database='./movie_database.sqlite3'    
)

mocha = movie_chatterbot  # Giving a friendly-sounding alias



if training_mocha:
    mocha.set_trainer(ListTrainer)
    mocha.train(dialogue_list[:10000])



mocha.read_only = True
print(mocha.read_only)



# List to store the conversation
conversation_record = []

# Initialize the conversation with cleverbot
mocha_response = ""
cleverbot_state = ""


for interaction in range(1,101):
    cleverbot_response, cleverbot_state, res_json = interact_cleverbot(mocha_response, cleverbot_state)
    mocha_response = mocha.get_response(cleverbot_response).text
    
    print("Cleverbot: ", cleverbot_response)
    print("Mocha: ", mocha_response)    
    print()
    
    conversation_record.append((interaction,'cleverbot',cleverbot_response))
    conversation_record.append((interaction,'mocha',mocha_response))    



with open("cleverbot_mocha_interactions.csv",'w',newline='') as csvfile:
    recordwriter = csv.writer(csvfile)
    for record in conversation_record:
        recordwriter.writerow(record)
