class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        while len(tokens)>0:
            if tokens[0]=="+":
                stack = stack[:-2]+[stack[-2]+stack[-1]]
            elif tokens[0]=="-":
                stack = stack[:-2]+[stack[-2]-stack[-1]]
            elif tokens[0]=="*":
                stack = stack[:-2]+[stack[-2]*stack[-1]]
            elif tokens[0]=="/":
                stack = stack[:-2]+[int(stack[-2]/stack[-1])]
            else:
                stack.append(int(tokens[0]))
            tokens = tokens[1:]
        return stack[0]