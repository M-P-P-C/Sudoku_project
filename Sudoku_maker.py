# packages
import numpy as np

#variables
test_sudoku=np.array([[1,2,3,4,5,6,7,8,9],[4,5,6,7,8,9,1,2,3],[7,8,9,1,2,3,4,5,6],
[6,7,8,9,1,2,3,4,5],[9,1,2,3,4,5,6,7,8],[3,4,5,6,7,8,9,1,2],
[2,3,4,5,6,7,8,9,1],[5,6,7,8,9,1,2,3,4],[8,9,1,2,3,4,5,6,7]])

false_sudoku=np.array([[1,2,3,4,5,7,7,8,9],[4,5,6,7,8,9,1,2,3],[7,7,9,1,2,3,4,5,6],
[1,2,3,4,5,6,7,8,9],[4,5,6,7,8,9,1,2,3],[7,8,9,1,2,3,4,5,6],
[1,2,3,4,5,6,7,8,9],[4,5,6,7,8,9,1,2,3],[7,8,9,1,2,3,4,5,6]])

zero_sudoku = np.zeros([9, 9], dtype=int)

#checkers functions

#checker 1: lines
def sudoku_line_checker(SUDOKU,SIZE):
    '''
    sudoku: the inputting sudoku as an array
    size: the amount of digits in a row
    '''

    status = False

    #iterating through the lines of the sudoku
    for i in range(SIZE):  
        suspect=SUDOKU[i]
        #exclude missing inputs
        suspect=suspect[suspect !=0]
        
        #check if there are duplicates
        _,data = np.unique(suspect, return_counts=True)
        if True in (data>1):
            return status

    status = True
    return status

#checker 2: columns            
def sudoku_column_checker(SUDOKU,SIZE):
    '''
    sudoku: the inputting sudoku as an array
    size: the amount of digits in a row
    '''

    status = False
    
    #iterate through columns
    for i in range(SIZE):
        suspect=SUDOKU[:,i]
        #exclude missing inputs
        suspect=suspect[suspect !=0]
        
        #check if there are duplicates
        _,data = np.unique(suspect, return_counts=True)
        if True in (data>1):
            return status
    
    status = True
    return status

#checker 3: squares
def sudoku_square_checker(SUDOKU,SIZE):
    '''
    sudoku: the inputting sudoku as an array
    size: the amount of digits in a row
    '''

    status = False
    squrt = int((SIZE)**0.5)

    #iterating through the squares
    for i in range(1,squrt+1):
        for j in range(1,squrt+1):
            suspect=SUDOKU[((j-1)*squrt):(j*squrt),((i-1)*squrt):(i*squrt)]            
            #exclude missing inputs
            suspect=suspect[suspect !=0]
            
            #check if there are duplicates
            _,data = np.unique(suspect, return_counts=True)
            if True in (data>1):
                return(status)

    status = True
    return status

#checker 4: correct amount of digits in the sudoku
def sudoku_total_checker(SUDOKU, SIZE):
    '''
    sudoku: the inputting sudoku as an array
    size: the amount of digits in a row
    '''

    status = False
    
    suspect=SUDOKU
    suspect=suspect[suspect !=0]
    _,data = np.unique(suspect, return_counts=True)
    if True in (data>SIZE):
        return(status)

    status = True
    return status

def sudoku_cheker(sudoku,size=9, total = True, line = True, column = True, square = True):
    
    results = {}

    if total == True:
        results["total"] = sudoku_total_checker(SUDOKU=sudoku, SIZE=size)
    if line == True:
        results["line"] = sudoku_line_checker(SUDOKU=sudoku, SIZE=size)
    if column == True:
        results["column"] = sudoku_column_checker(SUDOKU=sudoku, SIZE=size)
    if square == True:
        results["square"] = sudoku_square_checker(SUDOKU=sudoku, SIZE=size)

    for i in results.keys():
        if results[i]==False:
            print("false sudoku")
            break
        else:
            if i == list(results.keys())[-1]:
                print ("working sudoku")


    return results
    
for i in [test_sudoku,false_sudoku,zero_sudoku]:
    results = sudoku_cheker(i)
    print (results)




'''
next steps
DONE    whole sudoku, right amount of digits? (20.05.)
DONE    excluded default message "computed" from single functions and other minor smoothing factors (20.05.)
DONE    superfunction to combine the checker functions (20.05.)
    functions can be turned on and off
    size of sudoku can be adjusted
'''

    

print (test_sudoku)
print(false_sudoku)

