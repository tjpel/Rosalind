"""
Author: Thomas Pelowitz
    Website: https://www.tpelowitz.com
    Github: https://www.github.com/tjpel
Date: 29NOV23

Problem link: https://rosalind.info/problems/fibd/
"""

import numpy as np

class IEV():
    def __init__(self, input_string):
        self.n, self.m = (int(i) for i in input_string.split(" "))

    def solve(self):
        #O(n^2) to satify dynamic :(
        table = np.zeros([self.n+1,self.m], dtype=np.int64)
        table[1][0] = 1

        for month in range(2, table.shape[0]):
            for age in range(table.shape[1]):
                if age == 0: #newborns
                    table[month][age] = np.sum(table[month-1][1:]) #one for every adult from last month
                else: #was alive last month
                    table[month][age] = table[month-1][age-1] #another month older

        return np.sum(table[self.n])

print(IEV("90 19").solve())