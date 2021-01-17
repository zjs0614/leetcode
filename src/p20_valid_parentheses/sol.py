class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses_open = ['(', '{', '[']
        parentheses_close = [')', '}', ']']
        for c in s:
            if c in parentheses_open:
                stack.append(c)
            elif c in parentheses_close:
                c1 = stack.pop() if len(stack) > 0 else None
                if c1 is None or parentheses_open.index(c1) != parentheses_close.index(c):
                    return False
        return len(stack) == 0
