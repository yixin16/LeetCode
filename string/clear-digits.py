class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for char in s:
            if char.isdigit():
                if stack:
                    stack.pop()  # remove the previous non-digit character
            else:
                stack.append(char)
        return ''.join(stack)
