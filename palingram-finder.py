# dictionary imported from https://greenteapress.com/thinkpython2/code/words.txt\
import os

dictionary = []
try:
    with open(os.path.dirname(os.path.abspath(__file__)) + '/dictionary.txt') as file:
        for line in file:
            dictionary.append(line.rstrip('\r\n'))
        file.close()
except IOErrror as e:
    print('{}\nError opening {}. Terminating program.' .format(e, file), file.sys.stderr)
    sys.exit(1)
