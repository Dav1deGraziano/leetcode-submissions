class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        if n==1:
            return ["()"]
        elif n==2:
            return ["()()","(())"]
        else:
            to_be_completed = self.generateParenthesis(n-1)
            res = ["()"*n]
            for s in to_be_completed[0:-1]:
                i = 0
                while i<2*(n-1)-1:
                    if s[i]==")":
                        i += 1
                        continue
                    residual = 1
                    for j in range(i+1,2*(n-1)):
                        if s[j]==")":
                            residual -= 1
                            if residual<0:
                                break
                            elif residual == 0:
                                if i==0:
                                    if "("+s[:j+1]+")"+s[j+1:] not in res:
                                        res.append("("+s[:j+1]+")"+s[j+1:])
                                else:
                                    if s[:i]+"("+s[i:j+1]+")"+s[j+1:] not in res:
                                        res.append(s[:i]+"("+s[i:j+1]+")"+s[j+1:])
                        else:
                            residual += 1
                    i += 1
            res.append("("+to_be_completed[-1]+")")

        return res
        