#!/usr/bin/env python3

import numpy as np 
from numpy.random import default_rng #used to generate random square without repetition
import sudoku_checker as sudokucheck
import time


rng = default_rng() #setup random number generator


def main():

    size_square = 3

    numbers = np.arange(1, 1+size_square**2) #possible numbers in a NxN square

    sudoku = sudoku_init(numbers, size_square)

    #sudoku = num_filler(sudoku)
    start = time.time()
    timess = []
    for i in range(1000000):
        check = berkley_test(sudoku, start, timess)

        if check != None:
            start = time.time()




    squares_to_fill = [(1,2), (2,1), (2,3)] #coordinates of squares to be filled with full random squares

    start = time.time()
    for x, y in squares_to_fill: #This loop fills out desired squares with working sudoku number combinations

        line = False #initialize boolean variables
        column = False

        while line == False or column == False:
            sudoku_temp = sudoku_fill(sudoku.copy(), numbers, x, y, size_square)
            line, column = sudokucheck.full_sudoku_check(sudoku_temp,)

        sudoku = sudoku_temp.copy()

    end = time.time()
    print('Time elapsed to fill sudoku: '+str(end - start)+' seconds \n')

    #print(sudoku)

    import sudoku_visualizer

    sudoku_visualizer.command_line_sud(sudoku)



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
    #sudoku[pos[3], pos[3]] = small_squares[2,:,:]

    #from matplotlib import pyplot as plt
    #plt.imshow(sudoku, interpolation='nearest')
    #plt.show()

    return sudoku

def sudoku_fill(sudoku_temp, numbers,  sq_to_fill_x, sq_to_fill_y,size_square = 3):
    #Iterates over the sudoku to fill out the missing squares to output a potential candidate

    pos = {}
    for i in range(size_square):
        pos[i+1] = slice(i*size_square,(i+1)*size_square)

    new_square = random_square(numbers, size_square)

    sudoku_temp[pos[sq_to_fill_x], pos[sq_to_fill_y]] = new_square

    '''if sudoku_temp[0,3] == 0:
        sudoku_temp[0:3,3:6] = new_square
    elif sudoku_temp[3,0] == 0:
        sudoku_temp[3:6,0:3] = new_square
    elif sudoku_temp[3,6] == 0:
        sudoku_temp[3:6,6:9] = new_square
    elif sudoku_temp[6,3] == 0:
        sudoku_temp[6:9,3:6] = new_square'''


    return sudoku_temp

def berkley_test(sudoku, start, timess):
    sudoku2 = sudoku.copy()
    try:
        rows    = [set(range(1,10)) for i in range(9)] # set of available
        columns = [set(range(1,10)) for i in range(9)] #   numbers for each
        squares = [set(range(1,10)) for i in range(9)] #   row, column and square

        for i in range(9):
            rows[i].discard(rows[i].difference_update(sudoku[i]))
            columns[i].discard(columns[i].difference_update(sudoku[:,i]))
            squares[0+int(i/3)*4].discard(squares[0+int(i/3)*4].difference_update(sudoku[i]))
            #for j in range(9):
                #columns[j].discard(columns[j].intersection(sudoku[:, j]))

        #empt = [[3,4,5,6,7,8],[0,1,2,6,7,8],[0,1,2,3,4,5]]
        empt = [[3,4,5,6,7,8],[0,1,2,6,7,8],[0,1,2,3,4,5,6,7,8]]
        #empt = [[3,4,5,6,7,8],[0,1,2,3,4,5,6,7,8],[0,1,2,3,4,5,6,7,8]]
        #empt = [[0,1,2,3,4,5,6,7,8],[0,1,2,3,4,5,6,7,8],[0,1,2,3,4,5,6,7,8]]
        cc=0
        import random
        for i in range(9):
            if i ==3 or i==6:
                #print(sudoku2)
                cc+=1
            for j in empt[cc]:
                # pick a number for cell (i,j) from the set of remaining available numbers
                
                    choices = rows[i].intersection(columns[j]).intersection(squares[int(i/3)*3 + int(j/3)])
                    choice  = random.choice(list(choices))

                    sudoku2[i][j] = choice

                    rows[i].discard(choice)
                    columns[j].discard(choice)
                    squares[int(i/3)*3 + int(j/3)].discard(choice)
                

        # success! every cell is filled.

        end = time.time()
        print('Time elapsed to fill sudoku: '+str(end - start)+' seconds \n')

        timess.append(end - start)
        start = time.time()

        return start

    except IndexError:
                # if there is an IndexError, we have worked ourselves in a corner (we just start over)
        pass




if __name__ == "__main__":
    main()

