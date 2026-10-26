
class Solution:
    def customSortString(self, order: str, s: str) -> str:

        new = {}
        no = len(order)
        for i in range(no):
            new[order[i]] = i
        for i in range(26):
            l = chr(i+ord('a'))
            if l not in new:
                new[l] = no
                no += 1
        
        res = [[new[s[i]],s[i]] for i in range(len(s))]
        res.sort(key=lambda x: x[0])
        ans = "".join(x[1] for x in res)

        return ans


        

        