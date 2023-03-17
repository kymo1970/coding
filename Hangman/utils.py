import random
import csv

words = open(file="list.csv")
words.read()


def getWord():
    wordList = []
    for word  in words:
#        stripWord = word.strip()
#        print(stripWord)
        wordList.append(word)

#    print(wordList)
    
    disWord = random.choice(wordList)
    return disWord

