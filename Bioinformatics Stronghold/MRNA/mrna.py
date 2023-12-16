"""
Author: Thomas Pelowitz
    Website: https://www.tpelowitz.com
    Github: https://www.github.com/tjpel
Date: 30NOV23

Problem link: https://rosalind.info/problems/mrna/
"""

CODON_TABLE = {
    'A': ['GCA', 'GCC', 'GCG', 'GCT'],
    'C': ['TGC', 'TGT'],
    'D': ['GAC', 'GAT'],
    'E': ['GAA', 'GAG'],
    'F': ['TTC', 'TTT'],
    'G': ['GGA', 'GGC', 'GGG', 'GGT'],
    'H': ['CAC', 'CAT'],
    'I': ['ATA', 'ATC', 'ATT'],
    'K': ['AAA', 'AAG'],
    'L': ['CTA', 'CTC', 'CTG', 'CTT', 'TTA', 'TTG'],
    'M': ['ATG'],
    'N': ['AAC', 'AAT'],
    'P': ['CCA', 'CCC', 'CCG', 'CCT'],
    'Q': ['CAA', 'CAG'],
    'R': ['AGA', 'AGG', 'CGA', 'CGC', 'CGG', 'CGT'],
    'S': ['AGC', 'AGT', 'TCA', 'TCC', 'TCG', 'TCT'],
    'T': ['ACA', 'ACC', 'ACG', 'ACT'],
    'V': ['GTA', 'GTC', 'GTG', 'GTT'],
    'W': ['TGG'],
    'Y': ['TAC', 'TAT'],
    '_': ['TAA', 'TAG', 'TGA'],
}

class MRNA():
    ONEMIL = 1000000

    def __init__(self, prot_str):
        self.prot_str = prot_str

    def solve(self):
        total_mod_1mil = 1

        for aa in self.prot_str:
            total_mod_1mil *= len(CODON_TABLE[aa])
            total_mod_1mil %= ONEMIL

        return (total_mod_1mil * 3) % ONEMIL #stop codon

with open("rosalind_mrna.txt", "r") as f:
    prot_str = f.read().strip()

print(MRNA(prot_str).solve())

    

