from typing import List

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # 12345
        # 123 -> 132
        # 132 -> 213
        nums = [i for i in range(1, n+1)]
        for _ in range(1, k):
            self.next_perm(nums)
        ans = ""
        for each in nums:
            ans += str(each)
        return ans

    

    def next_perm(self, nums: List[int]) -> None:
        # print("input", nums)
        i = len(nums) - 2

        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            nums[j], nums[i] = nums[i], nums[j]

        self.reverse(nums, i+1, len(nums) - 1)
        # print("output", nums)
    

    def reverse(self, nums: List[int], start:int, end: int):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

        