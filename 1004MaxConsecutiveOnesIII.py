from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        zero_count = 0
        ans = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zero_count += 1
            while zero_count > k:
                if nums[l] == 0:
                    zero_count -= 1
                l += 1
            ans = max(ans, r - l + 1)

        return ans

# manual testing
if __name__ == "__main__":
    sol = Solution()
    nums = [1,1,1,0,0,0,1,1,1,1,0]
    k = 2
    result = sol.longestOnes(nums, k)
    print(result)