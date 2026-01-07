class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1)!=set(word2):
            return False
        dict1 = {}
        for char in word1:
            if char in dict1:
                dict1[char]+=1
            else:
                dict1[char]=1
        dict2 = {}
        for char in word2:
            if char in dict2:
                dict2[char]+=1
            else:
                dict2[char]=1
        if sorted(dict1.values())==sorted(dict2.values()):
            return True
        return False