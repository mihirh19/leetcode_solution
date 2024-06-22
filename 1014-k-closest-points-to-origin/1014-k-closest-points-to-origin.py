import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        for p in points:
            an = math.sqrt((p[0]**2 + p[1]**2))
            dist.append((an, p[0], p[1]))
        ans= []
        heapq.heapify(dist)
        for _ in range(k):
            _, x, y = heapq.heappop(dist)
            ans.append((x,y))
        return ans