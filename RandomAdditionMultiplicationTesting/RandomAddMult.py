import random
from datetime import date
import os

from CalculationMode import CalculationMode
from GameMode import GameMode


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

def getFileName():
    return 'results.txt'

# creates a file to write the results of the test
# new_file_name = '{}_{}_test.txt'.format(str(date.today()), mode_input)
# if not os.path.exists('./results'):
#     os.mkdir('./results')
# file_path = './results/' + new_file_name

def startGameMode(gameMode: GameMode):
    with open(gameMode.filename, 'a') as file:
        # initiates the test
        operand_pairs = []
        for i in range(gameMode.numberLimit):
            for j in range(gameMode.numberLimit):
                operand_pairs.append((i + 1, j + 1))

        random.shuffle(operand_pairs)

        for current_pair in operand_pairs:

            correct_answer = 0
            if gameMode.mode == CalculationMode.ADDITION:
                correct_answer = current_pair[0] + current_pair[1]
            elif gameMode.mode == CalculationMode.MULTIPLICATION:
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
                file.write('For {}\nguessed: {}, answer : {}\n\n'.format(question, guess, correct_answer))

def runGame():
    playerInput = chooseCalculationMode()
    filename = getFileName()
    gameMode = GameMode(playerInput, filename, 12)
    startGameMode(gameMode)

if __name__ == '__main__':
    # run main code here
    runGame()