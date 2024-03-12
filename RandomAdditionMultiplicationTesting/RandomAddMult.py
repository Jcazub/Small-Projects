import io
import random
from datetime import date
import os
from typing import List

from CalculationMode import CalculationMode
from Calculator import Calculator
from GameSettings import GameSettings
from Result import Result


def runGame():
    calculationMode = chooseCalculationMode()
    filename = getFileName()
    gameSettings = GameSettings(calculationMode, filename, 12)
    startGame(gameSettings)


# initiates the test
def startGame(gameSettings: GameSettings):
    with open(gameSettings.filename, 'a') as file:
        pairs = getRandomizedOperands(gameSettings)
        for current_pair in pairs:
            result = runCalculationSession(current_pair, gameSettings.mode)
            printResults(result, file)


def runCalculationSession(pair: tuple, mode: CalculationMode):
    answer = Calculator.calculate(pair, mode)
    question = Calculator.getQuestion(pair, mode)
    guess = getPlayerGuess(question)
    return Result(question, answer, guess)


def printResults(result: Result, file):
    if result.guess == result.answer:
        print("Correct")
    else:
        print("Incorrect. Correct answer was " + str(result.answer))
        file.write('{} For {}: guessed: {}, answer : {}\n'.format(
            date.today(), result.question, result.guess, result.answer))


def getPlayerGuess(question: str):
    while True:
        try:
            guess = int(input(question))
            break
        except ValueError:
            print("Invalid input, try again.")
    return guess


# chooses the mode, either addition or multiplication
def chooseCalculationMode() -> CalculationMode:
    mode = ''
    while not mode:
        mode_user_input = input("Choose a testing mode: (a)ddition or (m)ultiplication: ")
        mode = CalculationMode.getCalculationMode(mode_user_input)
    return mode


def getFileName():
    return 'results/results.txt'


# generates all combinations of numbers from 1 till the limit
def getRandomizedOperands(gameSettings: GameSettings) -> List[tuple]:
    operand_pairs = []
    if gameSettings.mode == CalculationMode.SQUARES:
        for i in range(gameSettings.numberLimit):
            operand_pairs.append((i + 1, i + 1))
    else:
        for i in range(gameSettings.numberLimit):
            for j in range(gameSettings.numberLimit):
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
