class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n  = len(isConnected)
        no = 0
        visit = [False]*n

        def dfs(node, isConnected,visit):
            visit[node] = True
            for i in range(len(isConnected)):
                if isConnected[node][i] and not visit[i]:
                    dfs(i,isConnected, visit)
            

        for i in range(n):
            if not visit[i]:
                no+=1
                dfs(i,isConnected,visit)
        
        return no