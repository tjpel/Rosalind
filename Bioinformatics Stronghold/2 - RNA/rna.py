"""
Author: Thomas Pelowitz
    Website: https://www.tpelowitz.com
    Github: https://www.github.com/tjpel
Date: 09NOV23

Problem link: https://rosalind.info/problems/rna/
"""

class RNA():
    def __init__(self, dnaString: str):
        self.dnaString: str = dnaString

    def solve(self) -> str:
        return self.dnaString.replace("T", "U")

with open("dnastrand.txt", "r") as f:
    rna = RNA(f.readline())

print(rna.solve())