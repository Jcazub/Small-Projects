# TODO record results

import random
import sys
from datetime import date
import os

# chooses the mode, either addition or multiplication
mode_input = input("Choose a testing mode: add(ition) or mult(iplication)")

if mode_input in 'addition':
    mode = '+'
elif mode_input in 'multiplication':
    mode = '*'
else:
    sys.exit("Invalid Mode. Must be either add(ition) or mult(iplication).")

# creates a file to write the results of the test
new_file_name = '{}_{}_test.txt'.format(str(date.today()), mode_input)

if not os.path.exists('./results'):
    os.mkdir('./results')

file_path = './results' + new_file_name

limit = 5

list1 = [i+1 for i in range(limit)]
list2 = [i+1 for i in range(limit)]

with open(file_path, 'w') as file:
    # initiates the test
    random.shuffle(list1)
    for index1 in range(limit):
        random.shuffle(list2)
        for index2 in range(limit):
            correct_answer = 0

            if mode == '+':
                correct_answer = list1[index1] + list2[index2]
            elif mode == '*':
                correct_answer = list1[index1] * list2[index2]

            question = '{} {} {}'.format(list1[index1], mode, list2[index2])
            guess = int(input(question + ' = '))

            if guess == correct_answer:
                print("Correct")
            else:
                print("Incorrect. Correct answer was " + str(correct_answer))
                file.write('For {}\nguessed: {}, answer : {}\n\n'.format(question, guess, correct_answer))
