#!/usr/bin/env python3

import numpy as np

def command_line_sud(sudoku):
    '''
    function to print a sudoku from a numpy array into the command line with visual help
    '''

    size = int(np.sqrt(len(sudoku)))

    #Calculate length of line divider
    divider = ''
    separator = '-'*3*size
    for i in np.arange(size-1):
        divider += separator+'+'
    divider += separator

    row = 1
    col= 1

    for i in sudoku:

        string_row = ''

        for j in i:

            string_row += ' '+str(j)+' '

            if col in np.arange(size, len(sudoku), size, dtype = int):
                string_row += '|'

            col += 1

        print(string_row)

        if row in np.arange(size, len(sudoku), size, dtype = int):

            print(divider)   

        
        row += 1
        col = 1


        