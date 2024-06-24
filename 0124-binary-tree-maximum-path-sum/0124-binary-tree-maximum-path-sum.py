# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans =[root.val]

        def dfs(root):
            if not root:
                return 0
            l  = dfs(root.left)
            r = dfs(root.right)
            l = 0 if l <0 else l
            r = 0 if r <0 else r

            ans[0] = max(ans[0], root.val + l + r)
            return root.val  + max(l,r)
        dfs(root)
        return ans[0]