class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        if len(words) !=len(s):
            return False
        
        sr = "".join([i[0] for i in words])

        return sr == s

