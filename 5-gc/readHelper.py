def readGC():
    fo = open("rosalind_gc.txt", "r")

    all = fo.read()
    seperated = all.replace("\n", "").split(">")

    for i in range(len(seperated)):
        seperated[i] = [">" + seperated[i][:13], seperated[i][13:]]

    print(seperated)
    

    fo.close()
    return seperated

readGC()
