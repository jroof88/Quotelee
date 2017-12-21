#Script to run each quote through algorithm to generate jsonOutput.py
import sys
sys.path.append("../")
import json
from nlp import process_input

f = open('quotes.json')

data = json.loads(f.read())
quotes = []
quote = {}
counter = 0

for d in data:
    if d['quoteAuthor'] == "":
        full_quote = d['quoteText'] + " - Unknown"
    else:
        full_quote = (d['quoteText'] + " - " + d['quoteAuthor']).replace(".", "")
    quote['quote'] = full_quote
    quote['tags'] = process_input(full_quote)
    quotes.append(quote)
    quote = {}
    counter+=1
    print(counter)
    
print("**********Done**********")
    
j = json.dumps(quotes)
outFile = open('jsonOutput.json', 'w')
outFile.write(j)