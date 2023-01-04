import random
import config
from wordFunctions import getWord
import mail

wordList = []

for i in range(10):
    wordList.append(getWord(random.randint(0, config.numberOfWords)))

mail.createMail(wordList)





"""
for i in range(10):
    print(getWord(random.randint(0, config.numberOfWords)))
"""