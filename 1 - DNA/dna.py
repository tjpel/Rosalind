class DNA():
    def __init__(self, dnaString):
        self.dnaString = dnaString

    def solve(self) -> list:
        return [self.dnaString.count(letter) for letter in ['A', 'C', 'G', 'T']]
    
    def printSolution(self, solution):
        for num in solution:
            print(str(num) + " ", end="")

with open("dnastrand.txt", "r") as f:
    dna = DNA(f.readline())

counts = dna.solve()
dna.printSolution(counts)