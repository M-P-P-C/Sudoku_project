#!/usr/bin/env python3

import numpy as np 
from numpy.random import default_rng #used to generate random square without repetition
import sudoku_checker as sudokucheck




rng = default_rng() #setup random number generator


def main():

    size_square = 3

    numbers = np.arange(1, 1+size_square**2) #possible numbers in a NxN square

    sudoku = sudoku_init(numbers, size_square)

    #sudoku = num_filler(sudoku)

    line = False
    column = False

    while line == False or column == False:
        sudoku_temp = sudoku_fill(sudoku.copy(), numbers)
        line, column = sudokucheck.full_sudoku_check(sudoku_temp)

    sudoku = sudoku_temp.copy()

    print(sudoku)

    import sudoku_visualizer

    sudoku_visualizer.command_line_sud(sudoku)

    line = False
    column = False

    while line == False or column == False:
        sudoku_temp = sudoku_fill(sudoku.copy(), numbers)
        line, column = sudokucheck.full_sudoku_check(sudoku_temp)

    sudoku = sudoku_temp.copy()

    print(sudoku)

    line = False
    column = False

    while line == False or column == False:
        sudoku_temp = sudoku_fill(sudoku.copy(), numbers)
        line, column = sudokucheck.full_sudoku_check(sudoku_temp)

    sudoku = sudoku_temp.copy()

    print(sudoku)

    line = False
    column = False

    while line == False or column == False:
        sudoku_temp = sudoku_fill(sudoku.copy(), numbers)
        line, column = sudokucheck.full_sudoku_check(sudoku_temp)

    sudoku = sudoku_temp.copy()

    print(sudoku)


def random_square(numbers, size_square = 3): 
    #This function generates a random 3 by 3 square without repetition

    ttsquare = np.zeros([size_square, size_square], dtype = int)

    ttsquare = rng.choice(numbers,  size=(size_square, size_square),replace=False) 

    return ttsquare


def sudoku_init(numbers, size_square = 3):
    #This function initializes a sudoku array

    sudoku = np.zeros([size_square*size_square, size_square*size_square], dtype=int) #initialize array of full sudoku

    small_squares = np.zeros((3, size_square, size_square))

    for i in range(3):
        small_squares[i,:,:] = random_square(numbers, size_square) #3D array containing prefilled squares

    #pos= {'A': slice(0,3), 'B': slice(3,6), 'C': slice(6,9)} #possible positions of squares in sudoku
    pos = {}
    for i in range(size_square):
        pos[i+1] = slice(i*size_square,(i+1)*size_square)


    #the following section fills out the sudoku array with the generated squares
    sudoku[pos[1], pos[1]] = small_squares[0,:,:]
    sudoku[pos[2], pos[2]] = small_squares[1,:,:]
    sudoku[pos[3], pos[3]] = small_squares[2,:,:]

    #from matplotlib import pyplot as plt
    #plt.imshow(sudoku, interpolation='nearest')
    #plt.show()

    return sudoku

def sudoku_fill(sudoku_temp, numbers):
    #Iterates over the sudoku to fill out the missing squares to output a potential candidate

    new_square = random_square(numbers)

    if sudoku_temp[0,3] == 0:
        sudoku_temp[0:3,3:6] = new_square
    elif sudoku_temp[3,0] == 0:
        sudoku_temp[3:6,0:3] = new_square
    elif sudoku_temp[3,6] == 0:
        sudoku_temp[3:6,6:9] = new_square
    elif sudoku_temp[6,3] == 0:
        sudoku_temp[6:9,3:6] = new_square


    return sudoku_temp

def sudoku_checker(sudoku,size=9): #checks sudoku

    wrong_r = 1
    wrong_c = 1

    #checker 1: the lines work
    for i in range(size):
        suspect=sudoku[i]
        suspect=suspect[suspect !=0]
        test,data = np.unique(suspect, return_counts=True)
        if True in (data>1):
            print("lines don't compute")
            wrong_r = 1
            break
        if i == max(range(size)):
            print ("lines computed")
            wrong_r = 0

    #checker 2: the columns work
    for i in range(size):
        suspect=sudoku[:,i]
        suspect=suspect[suspect !=0]
        test,data = np.unique(suspect, return_counts=True)
        if True in (data>1):
            print("columns don't compute")
            wrong_c = 1
            break
        if i == max(range(size)):
            print ("columns computed")
            wrong_c = 0

    return wrong_r, wrong_c



if __name__ == "__main__":
    main()

