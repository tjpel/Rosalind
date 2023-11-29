"""
Author: Thomas Pelowitz
    Website: https://www.tpelowitz.com
    Github: https://www.github.com/tjpel
Date: 09NOV23

Problem link: https://rosalind.info/problems/revc/
"""

from compliments import COMPLIMENTS as C

class REVC():
    def __init__(self, dnaString: str):
        self.dnaString: str = dnaString

    def solve(self) -> str:
        revc: str = ""

        for letter in self.dnaString:
            revc += C[letter]
            
        return revc[::-1]

with open("dnastrand.txt", "r") as f:
    rna = REVC(f.readline())

print(rna.solve())