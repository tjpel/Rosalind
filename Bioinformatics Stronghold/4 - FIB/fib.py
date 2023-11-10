"""
Author: Thomas Pelowitz
    Website: https://www.tpelowitz.com
    Github: https://www.github.com/tjpel
Date: 10NOV23

Problem link: https://rosalind.info/problems/fib/
"""

class FIB():
    def __init__(self, n: int, k: int):
        self.n: int = n
        self.k: int = k

    def solve(self) -> int:
        n = self.n
        k = self.k

        def recursive(n, k):
            if n == 1:
                return 1
            elif n == 2:
                return k
            
            oneGenAgo = recursive(n-1, k)
            twoGensAgo = recursive(n-2, k)

            if n <= 4:
                return oneGenAgo + twoGensAgo
            
            return oneGenAgo + (twoGensAgo * k)
        
        return recursive(n, k)


fib = FIB(30, 2)

print(fib.solve())