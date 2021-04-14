# dictionary imported from https://greenteapress.com/thinkpython2/code/words.txt\
import os

dictionary = []
with open(os.path.dirname(os.path.abspath(__file__)) + '/dictionary.txt') as file:
    for line in file:
        dictionary.append(line.rstrip('\\\r\n'))
    file.close()

for entry in dictionary:
    print(entry)
