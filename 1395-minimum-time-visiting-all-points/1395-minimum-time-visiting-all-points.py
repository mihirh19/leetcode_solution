class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        co = 0
        p1 = points[0]
        for i in range(len(points)):
            p2 = points[i]
            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]
            co += max(abs(dx), abs(dy))
            p1 = p2
        
        return co
