import os

exit, dictionary = 'y', []
with open(os.path.dirname(os.path.abspath(__file__)) + '/dictionary.txt') as file:
    for line in file:
        dictionary.append(line.rstrip('\\\r\n'))
    file.close()

while exit.lower() == 'y':
    print('OPTIONS------------------------------------------')
    print('1. List all palindromes in dictionary')
    print('2. List all words that are also 2-word palingrams')
    print('3. List two words that are palingrams')
    print('4. List all semordnilaps')
    print('5. (Temporary) correct formatting on dicitonary.txt')
    print()
    choice = input('Enter choice: ')

    if choice == '1':
        for word in dictionary:
            if word == word[::-1]:
                print(word)

    elif choice == '2':
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
    
    elif choice == '3':
        

    elif choice == '4':
        for word in dictionary:
            for semordnilap in dictionary:
                if word[::-1] == semordnilap and word != semordnilap:
                    print(word + ' -> ' + semordnilap)
                    break
                

    else:
        print('invalid choice')

    exit = input('Go again? (y/n): ')