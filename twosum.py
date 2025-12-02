from typing import List
# Solution using hash table
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {} # define dictionary variable for hash table
        for idx, elem in enumerate(nums):
            remain_value = target - elem
            if remain_value in lookup:
                return [lookup[remain_value],idx]
            lookup[elem] = idx

# manual testing
if __name__ == "__main__":
    sol = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    result = sol.twoSum(nums, target)
    print(result)