class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:

        n = len(heights)
        ans = [-1 for _ in range(len(queries))]
        r = [[] for _ in range(n)]   
        stack = []                   

        for i,(a,b) in enumerate(queries):
            if a>b:
                b,a = a,b
            if a==b or heights[a]<heights[b]:
                ans[i] = b
            else:
                r[b].append((heights[a],i))

        for i in range(n-1,-1,-1):
            
            for h,q in r[i]:
                start,end = 0,len(stack)-1
                while start<=end:
                    mid = (start+end)//2
                    if heights[stack[mid]]>h:
                        ans[q] = stack[mid]
                        start = mid+1
                    else:
                        end = mid-1

            while stack and heights[stack[-1]]<=heights[i]:
                stack.pop()
            stack.append(i)

        return ans