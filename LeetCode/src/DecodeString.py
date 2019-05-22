class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            if i == ']':
                code = []
                while (stack[-1] != '['):
                    code.append(stack.pop())
                code = code[::-1]
                stack.pop()

                num = []
                while (stack and stack[-1].isdigit()):
                    num.append(stack.pop())
                num = num[::-1]
                # print(num)
                newCode = []
                for _ in range(int("".join(num))):
                    newCode.extend(code)
                stack.append("".join(newCode))
            else:
                stack.append(i)
        # print(stack)
        return "".join(stack)




