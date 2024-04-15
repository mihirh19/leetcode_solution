class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        c = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        ls = []
        for word in words:
            ls.append("".join([c[ord(i)-97] for i in word]))
        
        return len(set(ls))
        