from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = set(["+", "-", "*", "/"])
        res = 0
        stack = []
        for i in range(len(tokens)):
            if tokens[i] not in operands:
                stack.append(int(tokens[i]))
            else:
                if stack:
                    a = stack.pop()
                    b = stack.pop()
                    match tokens[i]:
                        case "+":
                            res = a + b
                            stack.append(res)
                        case "-":
                            res = b - a
                            stack.append(res)
                        case "*":
                            res = a * b
                            stack.append(res)
                        case "/":
                            res = int(b / a)
                            stack.append(res)

        return stack[-1]