import numpy as np 
from numpy.random import default_rng #used to generate random square without repetition


numbers = [1,2,3,4,5,6,7,8,9] #possible numbers in a 3x3 square

rng = default_rng()

def random_square(numbers): #this function generates a random 3 by 3 square without repetition

    ttsquare = np.zeros([3,3], dtype = int)

    ttsquare = rng.choice(numbers,  size=(3, 3),replace=False) 

    return ttsquare


def sudoku_init(numbers):
    
    sudoku = np.zeros([9, 9], dtype=int) #initialize array of full sudoku

    square_d1 = random_square(numbers)

    square_d2 = random_square(numbers)

    #square_d3 = random_square(numbers)
    square_d3 = np.zeros([3,3],dtype=int)

    sudoku[0:3,0:3] = square_d1
    sudoku[3:6,3:6] = square_d2
    sudoku[6:9,6:9] = square_d3

    return sudoku

def sudoku_fill(sudoku_temp, numbers):

    new_square = random_square(numbers)

    if sudoku[0,3] == 0:
        sudoku_temp[0:3,3:6] = new_square
    elif sudoku[3,0] == 0:
        sudoku_temp[3:6,0:3] = new_square
    elif sudoku[3,6] == 0:
        sudoku_temp[3:6,6:9] = new_square
    elif sudoku[6,3] == 0:
        sudoku_temp[6:9,3:6] = new_square

    #count = 0
    #for i in sudoku_num:
    #    for j in i:
    #        sudoku_num[count][j] = j+1
    #        count += 1
        #count = 0

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
#sudoku = num_filler(sudoku)

sudoku = sudoku_init(numbers)

wrong_r = 1
wrong_c = 1

while wrong_r == 1 or wrong_c==1:
    sudoku_temp = sudoku_fill(sudoku.copy(), numbers)
    wrong_r, wrong_c = sudoku_checker(sudoku_temp)

sudoku = sudoku_temp.copy()

wrong_r = 1
wrong_c = 1

while wrong_r == 1 or wrong_c==1:
    sudoku_temp = sudoku_fill(sudoku.copy(), numbers)
    wrong_r, wrong_c = sudoku_checker(sudoku_temp)

wrong_r = 1
wrong_c = 1

sudoku = sudoku_temp.copy()

print(sudoku)

while wrong_r == 1 or wrong_c==1:
    sudoku_temp = sudoku_fill(sudoku.copy(), numbers)
    wrong_r, wrong_c = sudoku_checker(sudoku_temp)

wrong_r = 1
wrong_c = 1

sudoku = sudoku_temp.copy()


while wrong_r == 1 or wrong_c==1:
    sudoku_temp = sudoku_fill(sudoku.copy(), numbers)
    wrong_r, wrong_c = sudoku_checker(sudoku_temp)

sudoku = sudoku_temp.copy()


print(sudoku)

