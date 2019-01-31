#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 10:33:41 2018

@author: rishabhshetty
"""

import numpy as np 
trial_matrix = [[1,1,1], [1,1,1],[1,2,3]]
rhs_trial = []


## Input from the user for the matrix. 
#n = int(input('Please enter the number of rows: '))
#for i in range(n):
#    T = list(map(int, input('Enter row: ').split()))
#    trial_matrix.append(T)


print('\nThe matrix: ')
print(np.matrix(trial_matrix))


## Subtracting 2 lists from each other. 
def subtract_lists(x,y):
    new_l = []
    for i in range(len(x)):
        new_l.append(x[i] - y[i])
    return new_l

##Multiplying the list with a sclar
def multiply_scalar(row, multiple):
    temp = []
    for i in range(len(row)):
        temp.append(row[i] * multiple)
    return temp
    
##Replacing in a string
def replace_string(matrix,index,element):
    matrix.remove()
    1 
  

## Checking if all the rows left are just null
def check_if_allnull(matrix):
    for i in matrix:
        for j in i:
            if j != 0:
                return False
    return True

    
## Initiating a global variable for echelon matrix. 
echelon_matrix = []

## Finding the matrix pivot row and dividing it by the lead 
def find_pivot(trial):
    matrix_pivot = []
    new = []
    ## Finiding the matrix pivot row.
    for j in range(len(trial[0])):
        for i in range(len(trial)):
             if trial[i][j]!= 0:
                 var = trial[i][j]
                 matrix_pivot.append(trial[i])
                 break
        if matrix_pivot != []:
            break
#    print('this is the pivot row', matrix_pivot[0])
    trial.remove(matrix_pivot[0])
    new = [i/var for i in matrix_pivot[0]]
    new = [new]
#    print('This is the new matrix now', new)
    echelon_matrix.append(new[0])
    return trial


## Converting all the rows below it to 0 
def converting_rows(matrix):
    new_lead = echelon_matrix[-1]
    for i in range(len(new_lead)):
        if new_lead[i] != 0:
            col = i
            break

    trial = []
    for row in matrix:
        if row[col] == 0:
            trial.append(row)
        if row[col] != 0:
            if row[col]<0:
                temp = [i*row[col] for i in new_lead]

                temp_1 = subtract_lists(row, temp)
            if row[col] >0:
                temp = [i*row[col] for i in new_lead]
                temp_1 = subtract_lists(row, temp)
        try:
            trial.append(temp_1)
        except UnboundLocalError:
            pass
    return trial




## Looping through the matrix to get the echelon matrix
x = find_pivot(trial_matrix)
for i in range(len(trial_matrix)):
    y = converting_rows(x)
    if check_if_allnull(y):
        echelon_matrix += y
        break
    else:
        x = find_pivot(y)
    if check_if_allnull(x):
        echelon_matrix += x
        break

print('\nThe echelon matrix:')
print( np.matrix(echelon_matrix))

seen_row = []
for row in range(len(echelon_matrix)):
    temp = echelon_matrix[row]
    for col in range(len(echelon_matrix[0])):
        if echelon_matrix[row][col] == 1 and echelon_matrix[row] not in seen_row:
            seen_row.append(echelon_matrix[row])
            for i in range(len(echelon_matrix)):
                if i != row and echelon_matrix[i][col] != 0:
                    temp_1 = multiply_scalar(temp, echelon_matrix[i][col])
                    transformed_row = subtract_lists(echelon_matrix[i], temp_1)
                    echelon_matrix[i] = transformed_row
                        
                        

                    
print('\nThe final reduced matrix is: ')
print(np.matrix(echelon_matrix))
        

