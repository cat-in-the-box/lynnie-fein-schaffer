# This program will allow the user to generate a random noun, adjective, or verb

import random

user_name = input("What is your name?")
print("Hi " + user_name + "! This program will help you come up with random words.")


####################### Functions ############################
def word_generator ():
    word_type = input("What type of word would you like to generate? You can choose from a noun, a verb, or an adjective.")
    
    if word_type == "noun":
        nouns()
    elif word_type == "adjective":
        adjectives()
    elif word_type == "verb":
        verbs()


def nouns():
    noun = ["cat", "mailbox", "pasta", "Obama", "Florida"]
    print(random.choice(noun))

def adjectives():
    adjectives = ["happy", "funny", "depressed", "outraged", "ecstatic"]
    print(random.choice(adjectives))
    
def verbs():
    verbs = ["hit", "jump", "swim", "kicked", "drove"]
    print(random.choice(verbs))



######################### Main ###############################
word_generator()


