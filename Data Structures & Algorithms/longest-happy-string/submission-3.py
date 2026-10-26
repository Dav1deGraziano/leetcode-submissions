class Solution:

    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        if a == max(a,b,c):
            if b >= c:
                c1,c2,c3 = 'a','b','c'
            else:
                b,c = c,b
                c1,c2,c3 = 'a','c','b'
        elif b == max(a,b,c):
            if a >= c:
                a,b,c = b,a,c
                c1,c2,c3 = 'b','a','c'
            else:
                a,b,c = b,c,a
                c1,c2,c3 = 'b','c','a'
        else:
            if a>=b:
                a,b,c = c,a,b
                c1,c2,c3 = 'c','a','b'
            else:
                a,b,c = c,b,a
                c1,c2,c3 = 'c','b','a'
        
        arr1 = [c1,c2,c3]*c
        a,b = a-c,b-c
        arr2 = [c1,c2]*b
        a -= b

        idx = 0
        while a>0 and idx<3*c:
            if idx % 3 == 0:
                a -= 1
                arr1[idx] += c1
            elif idx % 3 == 1:
                add = min(2, a)              
                a -= add
                arr1[idx] += c1*add
            # FIX 2: removed the idx == 3*c-1 branch
            idx += 1
        
        idx = 0
        while a>0 and idx<2*b:
            arr2[idx] += c1
            a -= 1
            idx += 2                         

        if a>0:                              
            add = min(2, a)
            if arr2:
                arr2[-1] += c1*add
            elif arr1:
                arr1[-1] += c1*add
            else:
                arr1 = [c1*add]
        
        ans1 = ''.join(arr1) if arr1 else ''
        ans2 = ''.join(arr2) if arr2 else ''

        return ans1+ans2