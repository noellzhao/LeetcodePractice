class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u'}
        sliding_window = s[:k]
        max_vow=0
        for char in sliding_window:
            if char in vowels:
                max_vow+=1
        current_vow = max_vow
        
        for i in range(k,len(s)):
            l_char = 1 if s[i-k] in vowels else 0
            r_char = 1 if s[i] in vowels else 0
            current_vow = current_vow-l_char+r_char
            max_vow = max(max_vow,current_vow)
        return max_vow

# manual testing
if __name__ == "__main__":
    sol = Solution()
    s = "abciiidef"
    k = 3
    result = sol.maxVowels(s, k)
    print(result)

        