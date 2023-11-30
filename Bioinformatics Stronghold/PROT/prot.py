"""
Author: Thomas Pelowitz
    Website: https://www.tpelowitz.com
    Github: https://www.github.com/tjpel
Date: 29NOV23

Problem link: https://rosalind.info/problems/prot/
"""

from Bio.Seq import Seq

class PROT():
    def __init__(self, rna: str):
        self.rna = rna

    def solve(self) -> str:
        return Seq(self.rna).translate()

with open("rosalind_prot.txt", "r") as f:
    rna = f.readline()
    print(PROT(rna).solve())