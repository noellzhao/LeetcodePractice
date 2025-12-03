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


# Solution using two pointers + sorted list
'''
Idea: after sorting the whole list, use two pointers where one points to the beinning
of the list, another points to the end of the list.
if the sum of two elements they are pointing two is > target, then
    shift the right pointer one unit to the left
elif the sum is < than target then
    shift the left pointer one unit to the right
if the sum is = target then
    return [pointer1, pointer2]
'''
class TwoPointers:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create an empty hash table to store index-value mapping
        lookup = {}
        for idx, elem in enumerate(nums):
            if elem not in lookup:
                lookup[elem] = []
            lookup[elem].append(idx) # use list to store index(ices) in case there are duplicate values
        sorted_nums = sorted(nums)
        left_pointer = 0
        right_pointer = len(sorted_nums)-1
        while left_pointer<right_pointer:
            two_item_sum = sorted_nums[left_pointer] + sorted_nums[right_pointer]
            if two_item_sum > target:
                right_pointer -= 1
            elif two_item_sum < target:
                left_pointer += 1
            else:
                # handle cases where two elements are the same
                idx1 = lookup[sorted_nums[left_pointer]]
                if len(idx1)==1:
                    return idx1 + lookup[sorted_nums[right_pointer]][:1]
                else:
                    return idx1[:2]
                

                
# manual testing
if __name__ == "__main__":
    sol = Solution()
    nums = [2, 7, 15, 11]
    target = 9
    result = sol.twoSum(nums, target)
    print(result)