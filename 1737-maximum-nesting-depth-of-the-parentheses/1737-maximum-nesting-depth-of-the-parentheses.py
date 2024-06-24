class Solution:
    def maxDepth(self, s: str) -> int:
      depth= 0
      op =0
      for c in s:
        if c == "(":
          op +=1
        elif c ==")":
          op -=1
        depth = max(depth, op)

      return depth