class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0

        for r in range(k, len(arr)):
            if abs(arr[l] - x) > abs(arr[r] - x):
                l += 1

            elif abs(arr[l] - x) == abs(arr[r] - x):
                if arr[l] < arr[r]:
                    break
                l += 1
            
            else:
                break
        
        return arr[l:l+k]


        