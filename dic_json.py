import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def dictionary(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word,data.keys(),n=1))
        if yn == "Y":
            return data[get_close_matches(word,data.keys(),n=1)[0]]
        elif yn == "N":
            return "Please double check"
        else:
            return "We didn't find the defenition"
    else:
        return "We didn't find the defenition"

user_word = input("Enter a word: \n")
print("The defenition of {} is:".format(user_word))
print(dictionary(user_word ))
