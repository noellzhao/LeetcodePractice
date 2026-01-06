from typing import List
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        lst = [0]
        for idx in range(len(gain)):
            lst.append(lst[idx]+gain[idx])
        return max(lst)