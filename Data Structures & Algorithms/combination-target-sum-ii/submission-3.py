class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        
        if target in candidates:
            res = [[target]]
        else:
            res = []

        nums = [x for x in candidates if x<target]
        len_nums = len(nums)

        if not nums:
            return res

        ## initialise procedure
        nums.sort()

        current_level = [[nums[0]]]
        current_sums = [nums[0]]
        lists_of_remaining = [nums[1:]]
        max_index_nums = len(nums)-1
        i = 1

        while i<=max_index_nums:
            if nums[i] not in nums[:i]:
                current_level.append([nums[i]])
                current_sums.append(nums[i])
                lists_of_remaining.append(nums[i+1:])
            i = i+1
        
        
        ## algorithm
        while current_level:

            prev_sums = current_sums
            prev_level = current_level
            prev_lists_of_remaining = lists_of_remaining
            current_level = []
            current_sums = []
            lists_of_remaining = []

            max_index_prev_level = len(prev_level)-1
            i = 0

            while i<=max_index_prev_level:

                a = prev_lists_of_remaining[i]

                if not a:
                    i = i+1
                    continue

                max_index_a = len(a)-1
                sum_at_zeroth_remaining = prev_sums[i]+a[0]

                if sum_at_zeroth_remaining==target:
                    res.append(prev_level[i]+[a[0]])
                    i = i + 1
                    continue
                elif sum_at_zeroth_remaining<target:
                    current_level.append(prev_level[i]+[a[0]])
                    lists_of_remaining.append(a[1:])
                    current_sums.append(prev_sums[i]+a[0])
                else:
                    i = i+1
                    continue

                j = 1

                while j<=max_index_a:

                    if prev_sums[i]+a[j]==target:
                        res.append(prev_level[i]+[a[j]])
                        break
                    elif prev_sums[i]+a[j]>target:
                        break
                    elif prev_sums[i]+a[j]<target and a[j] not in a[:j]:
                        current_level.append(prev_level[i]+[a[j]])
                        lists_of_remaining.append(a[j+1:])
                        current_sums.append(prev_sums[i]+a[j])
                        j = j+1
                    else:
                        j = j+1

                i = i+1

        return res