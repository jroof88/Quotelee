from random import *
from db import get_collection, get_documents

def calculate_score(tags1, tags2):
    score = 0
    for tag in tags1:
        if tag in tags2:
            score+=1
    return score

def get_random(quotes):
    random = randint(0, len(quotes)-1)
    return quotes[random] 

def find_nearest_neighbor(arg):
    max_score = -1
    curr_score = 0
    output = []
    quotes = get_documents("quotelee", "quotes")
    
    for quote in quotes:
        curr_score = calculate_score(arg, quote['tags'])
        if curr_score == max_score:
            output.append(quote['_id'])
        elif curr_score > max_score:
            max_score = curr_score
            output = []
            output.append(quote['_id'])  
        
    if max_score == 0:
        return False    
    
    #If multiple quotes with max_score take random                  
    if len(output) > 0:
        output = get_random(output)
    else:
        output = output[0]
        
    return output
