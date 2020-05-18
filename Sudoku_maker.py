# packages
import numpy as np
# emptysudoku
sudoku = np.zeros([9,9], dtype=int)
#variables
#a = list(range(1,10))
#seed = np.random.randint(1,10)

test_sudoku=np.array([[1,2,3,4,5,6,7,8,9],[4,5,6,7,8,9,1,2,3],[7,8,9,1,2,3,4,5,6],
[6,7,8,9,1,2,3,4,5],[9,1,2,3,4,5,6,7,8],[3,4,5,6,7,8,9,1,2],
[2,3,4,5,6,7,8,9,1],[5,6,7,8,9,1,2,3,4],[8,9,1,2,3,4,5,6,7]])

false_sudoku=np.array([[1,2,3,4,5,7,7,8,9],[4,5,6,7,8,9,1,2,3],[7,8,9,1,2,3,4,5,6],
[1,2,3,4,5,6,7,8,9],[4,5,6,7,8,9,1,2,3],[7,8,9,1,2,3,4,5,6],
[1,2,3,4,5,6,7,8,9],[4,5,6,7,8,9,1,2,3],[7,8,9,1,2,3,4,5,6]])

zero_sudoku = np.zeros([9, 9], dtype=int)

#checkers functions
def sudoku_checker(sudoku,size=9):
    '''
    sudoku: the inputting sudoku as an array
    size: the amount of digits in a row
    '''

    #checker 1: the lines work
    for i in range(size):
        suspect=sudoku[i]
        suspect=suspect[suspect !=0]
        test,data = np.unique(suspect, return_counts=True)
        if True in (data>1):
            print("lines don't compute")
            break
        if i == max(range(size)):
            print ("lines computed")

    #checker 2: the columns work
    for i in range(size):
        suspect=sudoku[:,i]
        suspect=suspect[suspect !=0]
        test,data = np.unique(suspect, return_counts=True)
        if True in (data>1):
            print("columns don't compute")
            break
        if i == max(range(size)):
            print ("columns computed")


sudoku_checker(test_sudoku)
sudoku_checker(false_sudoku)
sudoku_checker(zero_sudoku)

    
    

 


    

print (test_sudoku)
print(false_sudoku)

