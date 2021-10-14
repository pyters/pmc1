import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        d = input("did you mean '%s' instead? Please ansrainwer Y for Yes and N for No." % get_close_matches(word, data.keys())[0])
        if d == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        if d == "N":
            return "The word does not exist, please double check" 
        else:
            return "We did not understand your entry"
    else:
        return "The word does not exist, please double check"
    python
word = input("Enter word: ")

out = translate(word)

if type(out) == list:
    for item in out:
        print(item)
else:
    print(out)