class Solution:
    def getSmallestString(self, s: str) -> str:
        li = list(s)

        for i in range(len(s)-1):
            if (int(li[i])%2) == (int(li[i+1])%2):
                if li[i] > li[i+1]:
                    li[i], li[i+1] = li[i+1], li[i]
                    break

        return ''.join(li)