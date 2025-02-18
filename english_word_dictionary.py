import json
import difflib
from difflib import get_close_matches
data = json.load(open('data.json'))
def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.capitalize() in data:
        return data[w.capitalize()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w.lower(), data.keys(), cutoff = 0.8)) > 0:
        yn = input('Did you mean %s instead? Enter Y if yes, N if No: ' % get_close_matches(w.lower(), data.keys())[0])
        if yn == 'Y':
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == 'N':
            return 'The word does not exist. Please double check.' 
        else:
            return 'We did not understand your entry.'
        
    else:
        return 'The word does not exist. Please double check it.'
word = input('Enter word: ')
output = translate(word)
if type(output) == list:
    for item in output:
        print (item)
else:
    print (output)
    










