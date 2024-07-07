class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        su=0
        for i in range(len(s)):
            j = t.index(s[i])
            su+=abs(i-j)
        return su