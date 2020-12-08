import random

word_list=["empire", "catapult", "vehicle"]

hangman_stages=['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']





print("Hello and welcome to the Hangman game")

random_word=random.choice(word_list)

word_to_guess=[]
print(random_word)
for i in range(len(random_word)):
    word_to_guess.append("_")

letter=input("Please quess letter: ")

if letter in random_word:
    print("yes")
    splitted=list(random_word)
    print(splitted)



