class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i == ']':
                if bool(stack) == False or stack[-1] == '(' or stack[-1] == '{':
                    return False
                else:
                    stack.pop()
            elif i == '}':
                if bool(stack) == False or stack[-1] == '(' or stack[-1] == '[':
                    return False
                else:
                    stack.pop()
            elif i == ')':
                if bool(stack) == False or stack[-1] == '{' or stack[-1] == '[':
                    return False
                else:
                    stack.pop()
            else:
                stack.append(i)

        if bool(stack) == False:
            return True

        return False
