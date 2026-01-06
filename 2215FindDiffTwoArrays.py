from typing import List
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        dict1 = set(nums1)
        dict2 = set(nums2)
        return [
            list(dict1-dict2),
            list(dict2 - dict1)
        ]