# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        s1 = []
        s2  = []
        if not root:
            return s2
        s1.append(root)

        while len(s1)!=0:
            tmp = s1.pop()
            s2.append(tmp)
            if tmp.left:
                s1.append(tmp.left)
            if tmp.right:
                s1.append(tmp.right)
            
        s2 = list(map(lambda x: x.val, s2))
        return s2[::-1]