from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict_freq = {}
        for num in arr:
            if num in dict_freq:
                dict_freq[num]+=1
            else:
                dict_freq[num]=1
        if len(dict_freq.values()) == len(set(dict_freq.values())):
            return True
        return False