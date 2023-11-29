"""
Author: Thomas Pelowitz
    Website: https://www.tpelowitz.com
    Github: https://www.github.com/tjpel
Date: 28NOV23

Problem link: https://rosalind.info/problems/hamm/
"""

class Hamm():
    def __init__(self, dna1:str, dna2:str):
        self.dna1: str = dna1
        self.dna2: str = dna2

    def solve(self) -> int:
        distance: int = 0

        for i in range(len(self.dna1)):
            if self.dna1[i] != self.dna2[i]:
                distance += 1

        return distance
    
with open("rosalind_hamm.txt", "r") as f:
    dnastands = f.readlines()

hamm = Hamm(dnastands[0], dnastands[1])
print(hamm.solve())