class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = [0] * len(queries)

        for i, [x, y, r] in enumerate(queries):
            for a, b in points:
                if (x - a) ** 2 + (y - b) ** 2 <= r ** 2:
                    ans[i] += 1

        return ans