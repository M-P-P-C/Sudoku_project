#!/usr/bin/env python3

# packages
import numpy as np


def main():

    #variables
    test_sudoku=np.array([[1,2,3,4,5,6,7,8,9],[4,5,6,7,8,9,1,2,3],[7,8,9,1,2,3,4,5,6],
    [6,7,8,9,1,2,3,4,5],[9,1,2,3,4,5,6,7,8],[3,4,5,6,7,8,9,1,2],
    [2,3,4,5,6,7,8,9,1],[5,6,7,8,9,1,2,3,4],[8,9,1,2,3,4,5,6,7]])

    false_sudoku=np.array([[1,2,3,4,5,7,7,8,9],[4,5,6,7,8,9,1,2,3],[7,7,9,1,2,3,4,5,6],
    [1,2,3,4,5,6,7,8,9],[4,5,6,7,8,9,1,2,3],[7,8,9,1,2,3,4,5,6],
    [1,2,3,4,5,6,7,8,9],[4,5,6,7,8,9,1,2,3],[7,8,9,1,2,3,4,5,6]])

    zero_sudoku = np.zeros([9, 9], dtype=int)

    for i in [test_sudoku,false_sudoku,zero_sudoku]:
        print (i)
        outcome_lines = sudoku_line_checker(i)
        outcome_columns = sudoku_column_checker(i)
        outcome_squares = sudoku_square_checker(i)


    print (test_sudoku)
    print(false_sudoku)

def full_sudoku_check(sudoku):
    outcome_lines = sudoku_line_checker(sudoku)
    print(outcome_lines)
    outcome_columns = sudoku_column_checker(sudoku)
    print(outcome_columns)
    outcome_squares = sudoku_square_checker(sudoku)
    print(outcome_squares)

    return outcome_lines, outcome_columns
#checkers functions

#checker 1: lines
def sudoku_line_checker(sudoku,size=9):
    '''
    sudoku: the inputting sudoku as an array
    size: the amount of digits in a row
    '''

    status = False
    message = "lines don't compute"

    #iterating through the lines of the sudoku
    for i in range(size):  
        suspect=sudoku[i]
        #exclude missing inputs
        suspect=suspect[suspect !=0]
        
        #check if there are duplicates
        _,data = np.unique(suspect, return_counts=True)
        if True in (data>1):
            print(message)
            return status

    status = True
    message = "lines computed"
    
    print (message)
    return status

#checker 2: columns            
def sudoku_column_checker(sudoku,size=9):
    '''
    sudoku: the inputting sudoku as an array
    size: the amount of digits in a row
    '''

    status = False
    message = ("columns don't compute")

    #iterate through columns
    for i in range(size):
        suspect=sudoku[:,i]
        #exclude missing inputs
        suspect=suspect[suspect !=0]
        
        #check if there are duplicates
        _,data = np.unique(suspect, return_counts=True)
        if True in (data>1):
            print(message)
            return status
        #if i == max(range(size)):
            #print ("columns computed")
    
    status = True
    message = "columns computed"
    print(message)
    return status

#checker 3: squares
def sudoku_square_checker(sudoku,size=9):
    '''
    sudoku: the inputting sudoku as an array
    size: the amount of digits in a row
    '''

    status = False
    message = "squares don't compute"
    squrt = int((size)**0.5)

    #iterating through the squares
    for i in range(1,squrt+1):
        for j in range(1,squrt+1):
            suspect=sudoku[((j-1)*squrt):(j*squrt),((i-1)*squrt):(i*squrt)]            
            #exclude missing inputs
            suspect=suspect[suspect !=0]
            
            #check if there are duplicates
            _,data = np.unique(suspect, return_counts=True)
            if True in (data>1):
                print (message)
                return(status)

    status = True
    message = "squares computed"
    print (message)
    return status






if __name__ == "__main__":
    main()