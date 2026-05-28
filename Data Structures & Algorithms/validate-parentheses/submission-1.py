class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")": "(", "]": "[", "}": "{"}

        for ch in s:
            if ch in "({[":
                stack.append(ch)
            elif ch in ")}]":
                if not stack or stack[-1] != pairs[ch]:
                    return False
                else:
                    stack.pop()
        
        return len(stack) == 0

        for ch in s:
            if ch in "({[":
                stack.append(ch)
            elif ch in ")}]":
                if stack is None or stack[-1] != pairs[ch]:
                    return False
                else:
                    stack.pop()

        return len(stack) == 0
