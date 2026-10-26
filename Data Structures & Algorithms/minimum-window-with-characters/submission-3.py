class Solution:
    def minWindow(self, s: str, t: str) -> str:

        def shortest_substring(lower: int, upper: int, dictionary: dict[str,int]) -> int:

            for k in range(lower,min(ns,upper+1)):
                if s[k] in dictionary:
                    dictionary[s[k]] -= 1
                    if dictionary[s[k]]==0:
                        del dictionary[s[k]]
                        if not dictionary:
                            return k
            
            return -1
            


        ns = len(s)
        nt = len(t)

        if nt>ns:
            return ""
        elif nt==1:
            return t if t[0] in s else ""
        
        dict_t = {}
        for ch in t:
            if ch in dict_t:
                dict_t[ch] += 1
            else:
                dict_t[ch] = 1
        
        dict_s = {}
        for ch in s:
            if ch in dict_t and ch in dict_s:
                dict_s[ch] += 1
            elif ch in dict_t and ch not in dict_s:
                dict_s[ch] = 1
        
        rel_dict = {}
        for ch in dict_t:
            if ch not in dict_s or dict_s[ch]<dict_t[ch]:
                return ""
            elif dict_s[ch]>dict_t[ch]:
                rel_dict[ch] = dict_s[ch]- dict_t[ch]
        
        res = None
        i = 0
        while i+nt-1<=ns-1:
            if s[i] in dict_t:
                if res is not None:
                    upper = shortest_substring(i,i+res-1,dict_t.copy())
                    if upper>=0 and upper-i+1<res:
                        res = upper-i+1
                        lower_res = i
                else:
                    upper = shortest_substring(i,ns-1,dict_t.copy())
                    lower_res = i
                    res = upper-i+1
            i += 1

        return s[lower_res:lower_res+res]

        