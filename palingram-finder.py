# dictionary imported from https://greenteapress.com/thinkpython2/code/words.txt\
import os

exit, dictionary = 'y', []
with open(os.path.dirname(os.path.abspath(__file__)) + '/dictionary.txt') as file:
    for line in file:
        dictionary.append(line.rstrip('\\\r\n'))
    file.close()

while exit.lower() == 'y':
    print('OPTIONS------------------------------')
    print('1. List all palindromes in dictionary')
    print('2. List all words that are palingrams')
    print('3. List two words that are palingrams')
    print()
    choice = input('Enter choice: ')

    if choice == '1':
        for word in dictionary:
            if word == word[::-1]:
                print(word)

    elif choice == '2':
        print('2')
        for word in dictionary:
            idx = 1
            while idx < len(word):
                

    else:
        print('invalid choice')

    exit = input('Go again? (y/n): ')