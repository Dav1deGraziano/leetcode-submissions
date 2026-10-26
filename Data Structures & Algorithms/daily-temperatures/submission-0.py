class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        n = len(temperatures)
        result = [0]*n
        queue = {str(temperatures[-1]): [temperatures[-1],n-1]}
        max_temperature_ahead = temperatures[-1]

        for i in range(n-1,-1,-1):
            if temperatures[i]>=max_temperature_ahead:
                queue = {str(temperatures[i]): [temperatures[i],i]}
                max_temperature_ahead = temperatures[i]
            else:
                index = n-1
                queue = {temp:queue[temp] for j,temp in enumerate(queue) if queue[temp][0]>temperatures[i]}
                for j,temp in enumerate(queue):
                    index = min(index,queue[temp][1])
                result[i] = index-i
                queue[str(temperatures[i])] = [temperatures[i],i]
            print(queue)
        
        return result



        