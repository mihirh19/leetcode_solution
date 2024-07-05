class Solution:
    def isPathCrossing(self, path: str) -> bool:
        loc = defaultdict(int)
        curr =[0,0]
        loc[tuple(curr)]+=1
        for s in path:
            if s=="N":
                curr[0]+=1
            elif s=="S":
                curr[0]-=1
            elif s=='E':
                curr[1]+=1
            elif s=='W':
                curr[1]-=1
            
            loc[tuple(curr)]+=1
            if loc[tuple(curr)]>1:
                return True
        
        return False
        