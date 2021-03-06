from random import *
from nlp import process_input
from knn import find_nearest_neighbor
from db import get_collection, get_documents

def fetch_quote(input_query):
    tags = process_input(input_query)
    result_id =  find_nearest_neighbor(tags)
    if result_id == False:
        return error_message()
    else:
        quote_collection = get_collection("quotelee", "quotes")
        quote_object = quote_collection.find_one({'_id': result_id})
        return quote_object
    
def error_message():
    people = ["Buddha", "Ralph Waldo Emerson", "Aristotle", "William Shakespeare"]
    adjectives = ["life", "sadness", "consciousness", "world"]
    rand1 = randint(0, len(people)-1)
    rand2 = randint(0, len(adjectives)-1)
    error_quote = {}
    error_quote['quote'] = "My apologies, I could not find a good match to your search query. Please check spelling or try stuff like \"" + people[rand1] + "\" or \"" + adjectives[rand2] + "\""
    error_quote['author'] = "No Match"
    return error_quote