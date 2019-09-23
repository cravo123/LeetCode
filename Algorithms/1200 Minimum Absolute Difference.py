# Solution 1, simulation
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        
        res = []
        curr_min = float('inf')
        
        for i in range(len(arr) - 1):
            val = arr[i + 1] - arr[i]
            if val == curr_min:
                res.append([arr[i], arr[i + 1]])
            elif val < curr_min:
                curr_min = val
                res = [[arr[i], arr[i + 1]]]
        return res