# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
    
        def dfs(root):
            if not root:
                return 0
            lft = dfs(root.left)
            if lft==-1:
                return -1
            rgt = dfs(root.right)
            if rgt==-1:
                return -1
            
            if abs(lft-rgt) >1:
                return -1
            return max(lft,rgt) +1
        return dfs(root) !=-1