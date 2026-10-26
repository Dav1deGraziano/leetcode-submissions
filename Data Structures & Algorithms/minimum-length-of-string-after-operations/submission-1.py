class Solution:
    def minimumLength(self, s: str) -> int:
        
        n = len(s)
        my_dict = {}
        for i in range(n):
            if s[i] not in my_dict:
                my_dict[s[i]] = [1,[i]]
            else:
                my_dict[s[i]][0] += 1
                my_dict[s[i]][1].append(i)
        
        deleted = 0
        for ch,val in my_dict.items():
            while my_dict[ch][0]>=3:
                my_dict[ch][0] -= 2
                my_dict[ch][1].pop()
                my_dict[ch][1][-2] = my_dict[ch][1][-1]
                my_dict[ch][1].pop()
                deleted += 2
        
        return n-deleted
