class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        neg_nums = []
        pos_nums = []
        for i in range(len(nums)):
            if nums[i]<=0:
                neg_nums.append(nums[i])
            else:
                pos_nums.append(nums[i])
        n_neg = len(neg_nums)
        n_pos = len(pos_nums)
        
        if neg_nums[-1:-4:-1]==[0,0,0]:
            res.append([0,0,0])

        i = 0
        while i<=n_neg-1 and neg_nums[i]<0:
            num_1 = neg_nums[i]
            if i>=1 and num_1==neg_nums[i-1]:
                i += 1
            else:
                j = i+1
                while j<=n_neg-1 and num_1+neg_nums[j]<=0:
                    num_2 = neg_nums[j]
                    if j>=i+2 and neg_nums[j]== neg_nums[j-1]:
                        j += 1
                    else:
                        crt_sum = num_1+num_2
                        for k in range(n_pos):
                            if crt_sum+pos_nums[k]==0:
                                res.append([num_1,num_2,pos_nums[k]])
                                break
                            elif crt_sum+pos_nums[k]>0:
                                break
                        j += 1

                j = 0
                for j in range(n_pos):
                    if j>=1 and pos_nums[j]==pos_nums[j-1]:
                        continue
                    else:
                        num_2 = pos_nums[j]
                        crt_sum = num_1+num_2
                        for k in range(j+1,n_pos):
                            if crt_sum+pos_nums[k]==0:
                                res.append([num_1,num_2,pos_nums[k]])
                                break
                            elif crt_sum+pos_nums[k]>0:
                                break
                i += 1
        
        return res