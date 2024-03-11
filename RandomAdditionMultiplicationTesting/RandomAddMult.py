import random
from datetime import date
import os
from typing import List

from CalculationMode import CalculationMode
from GameMode import GameMode


def runGame():
    playerInput = chooseCalculationMode()
    filename = getFileName()
    gameMode = GameMode(playerInput, filename, 12)
    startGameMode(gameMode)


# initiates the test
def startGameMode(gameMode: GameMode):
    with open(gameMode.filename, 'a') as file:
        pairs = getRandomizedOperands(gameMode)
        for current_pair in pairs:

            correct_answer = 0
            if gameMode.mode == CalculationMode.ADDITION:
                correct_answer = current_pair[0] + current_pair[1]
            elif gameMode.mode == CalculationMode.MULTIPLICATION or gameMode.mode == CalculationMode.SQUARES:
                correct_answer = current_pair[0] * current_pair[1]
            elif gameMode.mode == CalculationMode.SUBTRACTION:
                correct_answer = current_pair[0] - current_pair[1]
            elif gameMode.mode == CalculationMode.DIVISION:
                correct_answer = current_pair[0] // current_pair[1]

            question = '{} {} {}'.format(current_pair[0], gameMode.mode.getSign(), current_pair[1])
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
                file.write('{} For {}: guessed: {}, answer : {}\n'.format(
                    date.today(), question, guess, correct_answer))


# chooses the mode, either addition or multiplication
def chooseCalculationMode() -> CalculationMode:
    mode = ''
    while not mode:
        mode_user_input = input("Choose a testing mode: (a)ddition or (m)ultiplication: ")
        mode = getCalculationMode(mode_user_input)
    return mode


def getCalculationMode(mode: str):
    mode = mode.lower()
    if mode == 'a':
        return CalculationMode.ADDITION
    elif mode == 's':
        return CalculationMode.SUBTRACTION
    elif mode == 'm':
        return CalculationMode.MULTIPLICATION
    elif mode == 'x':
        return CalculationMode.SQUARES
    elif mode == 'd':
        return CalculationMode.DIVISION
    return None


def getFileName():
    return 'results/results.txt'


# generates all combinations of numbers from 1 till the limit
def getRandomizedOperands(gameMode: GameMode) -> List[tuple]:
    operand_pairs = []
    if gameMode.mode == CalculationMode.SQUARES:
        for i in range(gameMode.numberLimit):
            operand_pairs.append((i + 1, i + 1))
    else:
        for i in range(gameMode.numberLimit):
            for j in range(gameMode.numberLimit):
                operand_pairs.append((i + 1, j + 1))

    random.shuffle(operand_pairs)

    return operand_pairs


# creates a file to write the results of the test
# new_file_name = '{}_{}_test.txt'.format(str(date.today()), mode_input)
# if not os.path.exists('./results'):
#     os.mkdir('./results')
# file_path = './results/' + new_file_name


if __name__ == '__main__':
    # run main code here
    runGame()
