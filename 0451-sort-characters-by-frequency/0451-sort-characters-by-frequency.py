from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        di =dict( Counter(s))

        di = dict(sorted(di.items(), key=lambda x: x[1], reverse=True))

        an = ""
        for k,v in di.items():
            an +=str(k*v)
        return an

                