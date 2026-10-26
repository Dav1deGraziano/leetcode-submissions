class Solution:
    def simplifyPath(self, path: str) -> str:
        
        n = len(path)
        ans = []
        i = 0

        while i<n:

            if i+1<n and path[i+1] == '/':
                i += 1
                continue
            
            crt = ''
            while i+1<n and path[i+1] != '/':
                i += 1
                crt += path[i]
            
            if crt == '..':
                if ans:
                    ans.pop()
            elif crt and crt != '.':
                ans.append(crt)
            
            i += 1
        
        if not ans:
            return '/'
        
        return '/'+'/'.join(ans)
