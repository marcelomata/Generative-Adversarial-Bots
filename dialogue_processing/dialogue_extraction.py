# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 08:47:18 2017

@author: XingHan
"""
import pickle


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

pickle.dump(dialogue_list, open('dialogue_lines.p','wb'))
#==============================================================================
# with open('dialogue_lines.txt','w') as file:
#     for dialogue in dialogue_list:
#         file.write(dialogue)
#==============================================================================
        