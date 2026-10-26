class Solution:
    def candy(self, ratings: List[int]) -> int:

        n = len(ratings)
        candies = [1]*n
        i = 1
        if n>=2 and ratings[1]<ratings[0]:
            candies[0] += 1

        while i<n:
            if ratings[i]>ratings[i-1]:
                candies[i] = candies[i-1]+1
                i += 1
            elif i==n-1 or ratings[i+1]>=ratings[i]:
                i += 1
            else:
                j = 0
                while i+j+1<n and ratings[i+j+1]<ratings[i+j]:
                    j += 1
                for k in range(i+j-1,i-1,-1):
                    candies[k] = candies[k+1]+1
                if i-1>=0 and ratings[i-1]>ratings[i]:
                    candies[i-1] = max(candies[i-1],candies[i]+1)
                i += j+1
        
        print(candies)
        
        return sum(candies)
            
        