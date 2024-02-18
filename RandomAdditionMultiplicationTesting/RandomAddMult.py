import random
from datetime import date
import os

from CalculationMode import CalculationMode


def getCalculationMode(mode: str):
    mode = mode.lower()
    if mode in CalculationMode.ADDITION:
        return CalculationMode.ADDITION
    elif mode in CalculationMode.MULTIPLICATION:
        return CalculationMode.MULTIPLICATION
    elif mode in CalculationMode.SQUARES:
        return CalculationMode.SQUARES
    return None


# chooses the mode, either addition or multiplication
def chooseCalculationMode() -> CalculationMode:
    mode = ''
    while not mode:
        mode_user_input = input("Choose a testing mode: add(ition) or mult(iplication)")
        mode = getCalculationMode(mode_user_input)
    return mode


# creates a file to write the results of the test
new_file_name = '{}_{}_test.txt'.format(str(date.today()), mode_input)
if not os.path.exists('./results'):
    os.mkdir('./results')
file_path = './results/' + new_file_name

limit = 12

def getFile():
    #

with open(file_path, 'w') as file:
    # initiates the test
    operand_pairs = []

    for i in range(limit):
        for j in range(limit):
            operand_pairs.append((i + 1, j + 1))

    random.shuffle(operand_pairs)

    for current_pair in operand_pairs:

        correct_answer = 0

        if mode == '+':
            correct_answer = current_pair[0] + current_pair[1]
        elif mode == '*':
            correct_answer = current_pair[0] * current_pair[1]

        question = '{} {} {}'.format(current_pair[0], mode, current_pair[1])

        while True:
            try:
                guess = int(input(question + ' = '))
                break
            except ValueError:
                print("Invalid input, try again.")

        if guess == correct_answer:
            print("Correct")
        else:
            print("Incorrect. Correct answer was " + str(correct_answer))
            file.write('For {}\nguessed: {}, answer : {}\n\n'.format(question, guess, correct_answer))
