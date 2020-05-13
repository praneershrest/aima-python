#a1.py

from search import *
import random

def make_rand_8puzzle():
    randomList = random.sample(range(0,9), 9)
    newPuzzle = EightPuzzle(tuple(randomList))
    while(not newPuzzle.check_solvability(newPuzzle.initial)):
        randomList = random.sample(range(0,9), 9)
        newPuzzle = EightPuzzle(tuple(randomList))
    return newPuzzle
    
def display(state):
    index = 1
    for i in range(9):
        if(state[i] == 0):
            print('*', end = ' ')
        else:
            print(state[i], end = ' ')
        if(index%3 == 0):
            print()
        index += 1
        

puzzle = make_rand_8puzzle()
display(puzzle.initial)