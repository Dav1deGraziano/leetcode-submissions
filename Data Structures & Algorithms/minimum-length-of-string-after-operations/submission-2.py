class Solution:
    def minimumLength(self, s: str) -> int:
        
        n = len(s)
        my_dict = {}
        for i in range(n):
            if s[i] not in my_dict:
                my_dict[s[i]] = 1
            else:
                my_dict[s[i]] += 1
        
        deleted = 0
        for ch,val in my_dict.items():
            while my_dict[ch]>=3:
                my_dict[ch] -= 2
                deleted += 2
        
        return n-deleted
