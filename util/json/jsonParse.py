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
        author = "Unknown"
    else:
        author = d['quoteAuthor']
    quote['quote'] = d['quoteText']
    quote['author'] = author
    quote['tags'] = process_input(d['quoteText']) + author.lower().split(" ")
    print(d['quoteText'])
    quotes.append(quote)
    quote = {}
    counter+=1
    print(counter)
    
print("**********Done**********")
    
j = json.dumps(quotes)
outFile = open('jsonOutput.json', 'w')
outFile.write(j)