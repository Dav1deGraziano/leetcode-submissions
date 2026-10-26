class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        n_triplets = len(triplets)
        prev_triplet = [1,1,1]
        crt_triplet = [1,1,1]

        for i in range(n_triplets):
            prev_triplet = crt_triplet
            crt_triplet = [
                max(crt_triplet[0],triplets[i][0]),
                max(crt_triplet[1],triplets[i][1]),
                max(crt_triplet[2],triplets[i][2])
            ]
            if crt_triplet[0]==target[0] and crt_triplet[1]==target[1] and crt_triplet[2]==target[2]:
                return True
            elif crt_triplet[0]>target[0] or crt_triplet[1]>target[1] or crt_triplet[2]>target[2]:
                crt_triplet = prev_triplet
        
        return False

        