class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        copy = A
        # limit = 3*len(B)
        counter = 1

        while (len(A) <= 10000):
            if B in A:
                return counter
            else:
                A = A + copy
                counter += 1
        return -1
