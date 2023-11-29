"""
Author: Thomas Pelowitz
    Website: https://www.tpelowitz.com
    Github: https://www.github.com/tjpel
Date: 29NOV23

Problem link: https://rosalind.info/problems/grph/
"""

def parseInput(input_str):
    couples = []

    couples = input_str.split(" ")

    return couples

class IEV():
    def __init__(self, allele_string):
        self.couples = parseInput(allele_string)

    def solve(self):
        dominant_children = 0
        probabilities = [1, 1, 1, 0.75, 0.5, 0] #probability for each couple of having dominant child

        for i in range(len(self.couples)):
            dominant_children += int(self.couples[i]) * probabilities[i]

        return dominant_children * 2 #each couple has 2 kids

print(IEV("16001 17064 17900 18692 16869 16173").solve())