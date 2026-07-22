class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = {'+','-','*','/'}

        for ch in tokens:
            if ch not in operator:
                stack.append(int(ch))
            else:
                a = int(stack.pop())
                b = int(stack.pop())

                if ch == '+':
                    c = a + b
                elif ch == '-':
                    c = b - a
                elif ch == '*':
                    c= a* b
                elif ch == '/':
                    c = int(b / a)
                stack.append(c)
        return stack[-1]

        