class Solution:
    def mergeSimilarItems(self, items1: list[list[int]], items2: list[list[int]]) -> list[list[int]]:
        m1 = {value: weight for value, weight in items1}
        ret = []
        
        for item in items2:
            value, weight = item
            
            if not m1.get(value):
                m1[value] = weight
            else:
                m1[value] += weight
        
        for value, weight in m1.items():
            ret.append([value, weight])
        
        ret.sort()

        return ret