"""
Author: Thomas Pelowitz
    Website: https://www.tpelowitz.com
    Github: https://www.github.com/tjpel
Date: 09NOV23

Problem link: https://rosalind.info/problems/revc/
"""

from Bio import SeqIO

class GC():
    def __init__(self, dnaSeqs: dict):
        self.dnaSeqs: dict = dnaSeqs

    def solve(self):
        maxGC = {
            "SeqID": "",
            "GC Percent": 0
        }

        for id, seq in self.dnaSeqs.items():
            GCcount = seq.count('G') + seq.count('C')
            GCpercent = (GCcount / len(seq)) * 100

            if GCpercent > maxGC["GC Percent"]:
                maxGC["SeqID"] = id
                maxGC["GC Percent"] = GCpercent

        print(maxGC["SeqID"] + '\n' + str(maxGC["GC Percent"]))

seq_dict: dict = SeqIO.to_dict(SeqIO.parse("rosalind_gc.fasta","fasta"))
GC(seq_dict).solve()