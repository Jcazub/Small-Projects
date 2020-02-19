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

limit = 12

with open(file_path, 'w') as file:
    # initiates the test
    operand_pairs = []

    for i in range(limit):
        for j in range(limit):
            operand_pairs.append((i + 1, j + 1))

    random.shuffle(operand_pairs)

    print(operand_pairs)

    for current_pair in operand_pairs:

        correct_answer = 0

        if mode == '+':
            correct_answer = current_pair[0] + current_pair[1]
        elif mode == '*':
            correct_answer = current_pair[0] * current_pair[1]

        question = '{} {} {}'.format(current_pair[0], mode, current_pair[1])
        guess = int(input(question + ' = '))

        if guess == correct_answer:
            print("Correct")
        else:
            print("Incorrect. Correct answer was " + str(correct_answer))
            file.write('For {}\nguessed: {}, answer : {}\n\n'.format(question, guess, correct_answer))
