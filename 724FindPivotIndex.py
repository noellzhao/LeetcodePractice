from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sum = [0]
        for idx in range(len(nums)):
            prefix_sum += [prefix_sum[idx] + nums[idx]]
        for idx in range(len(nums)):
            if prefix_sum[idx+1]-prefix_sum[0]==prefix_sum[len(nums)]-prefix_sum[idx]:
                return idx
        return -1