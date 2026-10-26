class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        table = {}
        appeared = []
        res = 1

        for num in nums:
            if num not in appeared:
                table[str(num)] = num
                appeared.append(num)
        
        while table:
            key = list(table.keys())[0]
            crt_num = table[key]
            crt_len = 1
            del table[key]
            while str(crt_num-1) in table:
                crt_len += 1
                crt_num -= 1
                del table[str(crt_num)]
            crt_num = int(key)
            while str(crt_num+1) in table:
                crt_len += 1
                crt_num += 1
                del table[str(crt_num)]
            res = max(res,crt_len)
        
        return res
            
                
        

            