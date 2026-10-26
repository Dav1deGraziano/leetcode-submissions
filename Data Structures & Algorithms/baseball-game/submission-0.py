class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        queue = []

        for op in operations:

            if op == 'D':
                queue.append(queue[-1]*2)
            
            elif op == 'C':
                queue.pop()
            
            elif op == '+':
                queue.append(queue[-1]+queue[-2])
            
            else:
                queue.append(int(op))
        
        return sum(queue)
