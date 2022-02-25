# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Version:
    def __init__(self, bV: int):
        self.value = bV
    
    def isBad(self,n):
        if n >= self.value:
            return True
        return False


class Solution:
    def __init__(self, v: Version):
        self.version = v

    def isBadVersion(self,n):
        return self.version.isBad(n)

    def firstBadVersion(self, n: int) -> int:
        
        ini, end, maxfalse, mintrue = 1, n, 1, n
        pivot: int
        while (ini <= end):
            pivot = ini + (end-ini)//2
            if not self.isBadVersion(pivot):
                if pivot > maxfalse:
                    maxfalse = pivot
                ini = pivot+1
            else:
                if pivot < mintrue:
                    mintrue = pivot
                end = pivot-1
        return mintrue