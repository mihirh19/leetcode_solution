class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        li = s.split(" ")
        nw = li[:k]
        return " ".join(nw)