import numpy as np
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        x = np.zeros((len(grid)-2, len(grid[0])-2))
        def get3x3(grid, l,r):
            y = np.array(grid)
            ny = y[l:l+3, r:r+3]
            return np.amax(ny)

        
        for i in range(len(x)):
            for j in range(len(x[0])):
                x[i][j] = get3x3(grid, i,j)
        return list(x.astype(int))

        
