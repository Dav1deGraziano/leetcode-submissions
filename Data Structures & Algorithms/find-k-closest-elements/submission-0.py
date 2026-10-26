class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        n = len(arr)
        closest = []

        for start in range(n):
            if arr[start]>=x:
                if start-1>=0 and abs(x-arr[start-1])<=arr[start]-x:
                    start -= 1
                    break
        
        n_el = 1
        end = start

        while end-start+1<k:

            if end+1<n and start-1>=0:
                if abs(arr[start-1]-x)<=abs(arr[end+1]-x):
                    start -= 1
                else:
                    end += 1

            elif start-1>=0:
                start -= 1
            
            else:
                end += 1
        
        return arr[start:end+1]
        