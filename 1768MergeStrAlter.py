class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        max_len = max(len1,len2)
        result = []
        for i in range(max_len):
            if i < len1:
                result += [word1[i]]
            if i < len2:
                result += [word2[i]]
        return ''.join(result)
    
                
# manual testing
if __name__ == "__main__":
    sol = Solution()
    word1 = 'abc'
    word2 = 'pqr'
    result = sol.mergeAlternately(word1, word2)
    print(result)