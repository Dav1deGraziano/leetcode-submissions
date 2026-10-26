class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        n = len(s)
        window_length = 1+k
        res = min(window_length,n)
        i = 0

        while i<=n-res:
            
            appeared = []
            frequencies = []
            ## check most frequent characters
            for j in range(i,i+window_length):
                if s[j] in appeared:
                    frequencies[appeared.index(s[j])] += 1
                else:
                    appeared.append(s[j])
                    frequencies.append(1)

            max_frequency = max(frequencies)
            for ch in appeared:
                if frequencies[appeared.index(ch)]==max_frequency:
                    crt_len = 1+k
                    remaining = k-(1+k-max_frequency)
                    j = i+1+k
                    while remaining >= 0:
                        if j>n-1:
                            break
                        elif s[j]!=ch:
                            if remaining == 0:
                                break
                            else:
                                remaining -= 1
                        crt_len += 1
                        j += 1
                    res = max(res,crt_len)
            
            i += 1
        
        return res

            




        

            
        