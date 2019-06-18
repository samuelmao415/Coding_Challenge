# A left rotation operation on an array shifts each of the array's elements  unit to the left. For example, if  left rotations are performed on array , then the array would become .
#
# Given an array  of  integers and a number, , perform  left rotations on the array. Return the updated array to be printed as a single line of space-separated integers.
#
# Function Description
#
# Complete the function rotLeft in the editor below. It should return the resulting array of integers.
#
# rotLeft has the following parameter(s):
#
# An array of integers .
# An integer , the number of rotations.


#sample input:
# 5 4
# 1 2 3 4 5

#sample output:
# 5 1 2 3 4
import math
import os
import random
import re
import sys

a= [1,2,3,4,5]
d= 4
def rotLeft(a, d):
    indx = d
    front_values = a[indx:]
    new_list = []
    [new_list.append(value) for value in front_values]
    remaining_array = a[:indx]
    #new_list.append(front_values)
    [new_list.append(value) for inx, value in enumerate(remaining_array)]
    print(new_list)
    return(new_list)

rotLeft(a, d)
