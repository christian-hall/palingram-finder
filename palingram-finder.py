import os
import math

exit, dictionary = 'y', []
with open(os.path.dirname(os.path.abspath(__file__)) + '/dictionary.txt') as file:
    for line in file:
        dictionary.append(line.rstrip('\r\n'))
    file.close()

while exit.lower() == 'y':
    print()
    print('OPTIONS------------------------------------------')
    print('1. List all palindromes in dictionary')
    print('2. List two words that are palingrams')
    print('3. List all semordnilaps')
    print('4. List all words that are also multi-word semordnilaps')
    print()
    choice = input('Enter choice: ')

    if choice == '1':
        for word in dictionary:
            if word == word[::-1]:
                print(word)
    
    elif choice == '2':
        for first_word in dictionary:
            for second_word in dictionary:
                if (first_word + second_word) == (first_word + second_word)[::-1] and first_word != second_word:
                    print(first_word + ' ' + second_word)

    elif choice == '3':
        for word in dictionary:
            for semordnilap in dictionary:
                if word[::-1] == semordnilap and word != semordnilap:
                    print(word + ' -> ' + semordnilap)
                    break

    elif choice == '4':
        for word in dictionary:
            if len(word) > 3:
                palindrome, palingram, current_index = word[::-1], "", 1
                for character in palindrome:
                    palingram = palingram + character
                    if len(palingram) > current_index:
                        first_word, second_word = palingram, palindrome[len(palingram):len(word)]
                        for first_word_check_entry in dictionary:
                            if first_word_check_entry == first_word:
                                for second_word_check_entry in dictionary:
                                    if second_word_check_entry == second_word:
                                        print(word + ' -> ' + first_word + ' ' + second_word)
                        current_index = current_index + 1

        # get the maximum number of words that can fit inside this word (a word is at least two letters) and create an array of that size filled with "" strings
        # for: start with the smallest number of words that can fit in that array (word cap), then add one possible word until the maximum is reached
            # for: through each word and add one character until the character count is reached (starts at 2)
                # if the word is found in the dictionary, remove the taken characters and break the for loop to start on the next word
                # if the cap is reached, then the remaining words are added. 

                # will need to run an equation with each pass to ensure that the number of characters for each word will pass.
                        

    else:
        print('invalid choice')

    exit = input('Go again? (y/n): ')