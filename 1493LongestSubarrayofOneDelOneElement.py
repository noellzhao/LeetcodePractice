from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        ans = 0
        zero_count = 0
        for r in range(len(nums)):
            if nums[r]==0:
                zero_count += 1

            while zero_count > 1:
                if nums[l]==0:
                    zero_count-=1
                l+=1
            ans = max(ans,r-l)
        return ans