#!/usr/bin/env python
# -*-coding:utf-8-*-

"""
# File       : Hill_sort.py
# Time       ：2022/9/23 21:00
# Author     ：Michael
# version    ：python 3.10.7
# Description：
"""

"""
    stability: unstable
    Time complexity: related to the step size
"""

def shell_sort(alist):
    n = len(alist)  # length of the list
    gap =  n // 2   # step size (this step size may not be optimal)

    # gap changes to 0, the number of executions of the insertion algorithm
    while gap>0:
        # The starting value is from the beginning of the gap to the end of the length n of the list
        # The difference between Hill sorting and ordinary insertion sorting is the length of the gap
        for j in range(gap,n):
            #j = [gap+1,gap+2,gap+3 ....n-1]
            i = j
            # Subscript element to 0 cutoff
            while i>0:
                # If the current element is smaller than the value of the previous element, swap the positions of the two numbers
                if alist[i] < alist[i-gap]:
                    alist[i],alist[i-gap]=alist[i-gap],alist[i]
                    # The value of the subscript moves forward, minus a step value
                    i -= gap
                else:
                    break
        # After the current step cycle ends, shorten the current step
        gap//=2


if __name__ == '__main__':
    alist = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(alist)
    shell_sort(alist)
    print(alist) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

