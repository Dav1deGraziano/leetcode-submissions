class Solution:
    def reorganizeString(self, s: str) -> str:

        def insert_character(string: str, n: int, ch: str) -> str:

            for i in range(n-1):
                if string[i]!=ch and string[i+1]!=ch:
                    return string[:i+1] + ch + string[i+1:]
            
            return ""


        prev = ""
        res = ""
        queue = []
        
        for ch in s:
            if ch == prev:
                queue.append(ch)
            else:
                res += ch
                prev = ch
        
        l_queue = len(queue)
        n = len(s)-l_queue
        i = 0

        while i<l_queue:
            if res[-1]!=queue[i]:
                res += queue[i]
                n += 1
                l_queue -= 1
                queue.pop(i)
                i = 0
                continue
            dummy = insert_character(res,n,queue[i])
            if dummy:
                res = dummy
                n += 1
                l_queue -= 1
                queue.pop(i)
                i = 0
                continue
            i += 1
        
        return "" if queue else res

