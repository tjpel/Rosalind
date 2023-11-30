"""
Author: Thomas Pelowitz
    Website: https://www.tpelowitz.com
    Github: https://www.github.com/tjpel
Date: 30NOV23

Problem link: https://rosalind.info/problems/subs/
"""

class SUBS():
    def __init__(self, dna, motif):
        self.dna = dna
        self.motif = motif

    #could use native python methods for this, but this is more fun
    def solve(self):
        found_indexes = []

        for i in range(len(self.dna) - len(self.motif)):
            if self.dna[i:i+len(self.motif)] == self.motif:
                found_indexes.append(i+1) #answer requires conversion to 1-indexed

        return found_indexes

def print_solution(solution):
    for index in solution:
        print(str(index), end=" ")


with open("rosalind_subs.txt") as f:
    arguments = f.read().splitlines() #works to get rid of pesky newline chars

print(SUBS(arguments[0], arguments[1]).solve())

from Bio.Data import CodonTable
t=CodonTable.standard_dna_table
print(t.back_table["S"])