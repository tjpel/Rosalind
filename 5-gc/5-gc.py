import readHelper as help

def gc(dna: list) -> list:
    outList = ["", 0]

    for read in dna:
        if read == dna[0]:
            continue
        strand = read[1]
        gcRatio = (strand.count("G") + strand.count("C")) / len(strand)
        gcPer = gcRatio * 100
        if gcPer > outList[1]:
            outList = [read[0], gcPer]

    return outList

print(gc(help.readGC()))
