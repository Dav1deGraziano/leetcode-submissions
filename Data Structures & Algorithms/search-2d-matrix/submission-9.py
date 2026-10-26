class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def line_binary_search(row: List[int], target: int) -> tuple[bool, int]:
            if target<row[0]:
                return False, -1
            elif target==row[0]:
                return True, 0
            elif target>row[-1]:
                return False, 1
            elif target==row[-1]:
                return True, 0
            i = 0
            j = len(row)-1
            while i<=j:
                print(row[i:j+1])
                current_length=j-i
                if current_length+1==1 and target==row[i]:
                    return True, 0
                elif current_length+1==1 and target!=row[i]:
                    return False, 0
                else:
                    n_search = i+(current_length//2)
                    if target==row[n_search]:
                        return True, 0
                    elif target>row[n_search]:
                        i = n_search+1
                    else:
                        j = n_search-1
            if j<i:
                return False, 0

        i = 0
        j = len(matrix)-1
        while i<=j:
            n_search = i+((j-i)//2)
            res,within_range = line_binary_search(matrix[n_search],target)
            if res:
                return True
            else:
                if within_range==0:
                    return False
                elif within_range==-1:
                    j=n_search-1
                else:
                    i = n_search+1
        if j<i:
            return False

