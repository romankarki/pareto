from typing import List


class Solution:

    def min_abs_diff(self, arr: List[int]) -> List[int]:

        arr.sort()
        diff_dict = {}

        min_diff = float("inf")

        for i in range(0, len(arr) - 1):
            diff = arr[i+1] - arr[i]
            min_diff = min(diff, min_diff)

            if diff in diff_dict:
                diff_dict[diff].append([arr[i], arr[i+1]])
            else: 
                diff_dict[diff] = [[arr[i], arr[i+1]]]
            
        return diff_dict[min_diff]