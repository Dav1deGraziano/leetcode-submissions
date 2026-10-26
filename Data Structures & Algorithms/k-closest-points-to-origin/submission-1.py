import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        if not points[k:]:
            return points

        k_closest = points[0:k]
        distances = []
        
        for i in range(k):
            point = k_closest[i]
            distances.append(math.sqrt(point[0]**2+point[1]**2))

        max_dist = max(distances)
        max_dist_index = distances.index(max_dist)

        for point in points[k:]:
            distance = math.sqrt(point[0]**2+point[1]**2)
            if distance<max_dist:
                k_closest[max_dist_index] = point
                distances[max_dist_index] = distance
                max_dist = max(distances)
                max_dist_index = distances.index(max_dist)
        
        return k_closest