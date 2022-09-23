#!/usr/bin/env python
# -*-coding:utf-8-*-

"""
# File       : Bubble_Sort.py
# Time       ：2022/9/23 21:07
# Author     ：Michael
# version    ：python 3.10.7
# Description：
"""

"""
Algorithm description
 (1) Compare adjacent elements, if the first is larger than the second, swap;
 (2) Do the same operation for each pair of rural elements until the last pair, and the last element should be the largest number;
 (3) Loop steps (1) (2) until every pair of numbers needs to be compared.
"""


def bubble_sort(alist):
    n = len(alist)
    for i in range(0,n-1):
        # Mark, used for optimization, at this time the optimal time complexity is n, which is the number of inner loops.
        flag = 0
        # Why subtract i, because when the jth number is sorted to the last side, the next round will not follow the previously sorted data
        for j in range(0,n-1-i):
            if alist[j]>alist[j+1]:
                alist[j],alist[j+1] = alist[j+1],alist[j]
                # #If the position of the exchange data is realized, the flag is added by 1
                flag += 1
        # If flag is equal to 0, it means that the sequence does not implement data exchange, then exit
        if flag ==0:
            return alist
    return  alist
if __name__ == '__main__':
    alist = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(alist)
    bubble_sort(alist)
    print(alist) # [1, 2, 3, 4, 5, 6, 7, 8, 9]