class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = list()
        while len(strs)>=1:
            if len(strs)==1:
                sequence = list()
                sequence.append(strs[0])
                res.append(sequence)
                return res
            else:
                sequence = list()
                sequence.append(strs[0])
                a = list(strs[0])
                strs.remove(strs[0])
                i = 0
                while i<=len(strs)-1:
                    if len(strs[i])!=len(a):
                        i = i+1
                        continue
                    word = list(strs[i])
                    ok = True
                    for j in range(len(a)):
                        if a[j] not in word:
                            ok = False
                            break
                        word.remove(a[j])
                    if ok==True:
                        sequence.append(strs[i])
                        strs.remove(strs[i])
                        continue
                    else:
                        i = i+1
                res.append(sequence)
        return res
                    
            
        