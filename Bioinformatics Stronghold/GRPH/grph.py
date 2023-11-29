"""
Author: Thomas Pelowitz
    Website: https://www.tpelowitz.com
    Github: https://www.github.com/tjpel
Date: 29NOV23

Problem link: https://rosalind.info/problems/grph/
"""

from Bio import SeqIO

class GRPH():
    def __init__(self, dnaSeqs: dict, k: int = 3):
        self.dnaSeqs: dict = dnaSeqs
        self.k: int = k

    def solve(self):
        #make dict of all prefixs, then match to suffixs
        #O(2n), not sure if can be improved

        prefix_hash = {}

        #populate prefix hash
        for id, seq in self.dnaSeqs.items():

            prefix: str = str(seq.seq)[:self.k]

            if prefix in prefix_hash.keys(): #if theres an existing entry for that prefix
                prefix_hash[prefix].append(id) #add current id to that list
            else:
                prefix_hash[prefix] = [id] #make entry

        edges = []

        #match suffixes to prefixes
        for id, seq in self.dnaSeqs.items():

            suffix: str = str(seq.seq)[-self.k:]

            known_prefixs: list | None = prefix_hash.get(suffix)
            if known_prefixs:
                for kp in known_prefixs:
                    if kp != id:
                        edges.append([id, kp])

        return edges
                
seq_dict: dict = SeqIO.to_dict(SeqIO.parse("rosalind_grph.fasta", "fasta"))
solution: list = GRPH(seq_dict).solve()

with open("grph_answer.txt", "w") as f:
        f.writelines([f"{pair[0]} {pair[1]}\n" for pair in solution])