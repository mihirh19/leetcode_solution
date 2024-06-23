class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        par = {'(': ')', '{': '}', '[': ']'}

        for c in s:
            if c in par.keys():
                stack.append(c)

            elif c in par.values():
                if len(stack) == 0 or par[stack.pop()] != c:
                    return False

        return len(stack) == 0
