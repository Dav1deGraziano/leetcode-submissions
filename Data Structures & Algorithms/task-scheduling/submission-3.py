import numpy as np

class Solution:

    def leastInterval(self, tasks: List[str], n: int) -> int:

        if n == 0:
            return len(tasks)
        
        task_types = [tasks[0]]
        task_frequencies = [1]

        for task in tasks[1:]:
            if task not in task_types:
                task_types.append(task)
                task_frequencies.append(1)
            else:
                dummy_index = task_types.index(task)
                task_frequencies[dummy_index] = task_frequencies[dummy_index]+1
        

        highest_frequency = max(task_frequencies)
        highest_frequency_index = task_frequencies.index(highest_frequency)
        most_frequent_task = task_types[highest_frequency_index]

        idles = ["idle" for i in range(n)]
        base_queue = [most_frequent_task]+idles
        queue = []
        i = 1

        while i<=highest_frequency:
            queue.extend(base_queue)
            i = i+1
        
        
        task_types.pop(highest_frequency_index)
        task_frequencies.pop(highest_frequency_index)
        last_executed_index = np.zeros(len(task_types),dtype = int)


        while task_types:
            if "idle" not in queue:
                queue.extend(["idle"])
                first_idle = len(queue)-1
            elif last_executed_index[0] == 0:
                first_idle = queue.index("idle")
            else:
                first_idle_relative = queue[last_executed_index[0]+n+1:].index("idle")
                first_idle = first_idle_relative+len(queue[0:last_executed_index[0]+n+1])
                
            queue[first_idle] = task_types[0]
            if task_frequencies[0]-1==0:
                task_types = task_types[1:]
                task_frequencies = task_frequencies[1:]
                last_executed_index = last_executed_index[1:]
            else:
                task_frequencies[0] = task_frequencies[0]-1
                last_executed_index[0] = first_idle
        
        
        if "idle" in queue[-n-1:]:
            first_useless_idle = len(queue[0:-n-1]) + queue[-n-1:].index("idle")
            queue = queue[0:-n-1]+queue[-n-1:first_useless_idle]

        print(queue)
        
        return len(queue)
            

            

