#https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
import math
import os
import random
import re
import sys

n = 10
ar = [1, 1, 3, 1, 2, 1, 3, 3, 3, 3] #one pair of color one, one of color. three odd socks left. number of pairs is 2
n=9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

n=5
ar = [10.5,10.5,12,12,1]
def sockMerchant(n, ar):
    sorted_ar = sorted(ar)
    print('sorted: ',sorted_ar )
    pair_sum = 0
    index = 0
    while index +1 <n:
        if sorted_ar[index] == sorted_ar[index+1]:
            pair_sum +=1
            index +=2 #if there is a match, ignore the match ones
        else:
            index +=1 #if there is no match, match the current one with the next one

    return(pair_sum)

sockMerchant(n,ar)
