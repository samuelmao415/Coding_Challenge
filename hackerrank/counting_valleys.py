#https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
import math
import os
import random
import re
import sys

n =8
#s = 'UDDDUDUU'
s = 'DUUUUDDD'
len(s)
s.split()
# Complete the countingValleys function below.
def countingValleys(n, s):
    height = 0
    in_valley = False
    times_in_valley = 0
    for i in range(len(s)):
        if s[i] =='U':
            height += 1
        else:
            height -= 1

        if in_valley == False:
            if height < 0:
                in_valley = True
        elif height == 0:
            in_valley = False
            times_in_valley +=1
        print(height, in_valley,times_in_valley)

    return(times_in_valley)



countingValleys(n, s)
