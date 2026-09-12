class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        lastFound = {}
        maxLength = 1
        start = 0

        for i in range(0, len(s)):
            if s[i] in lastFound and lastFound[s[i]] >= start:
                # print(f"found {s[i]} in {str(lastFound)} at {i} with {start}")
                maxLength = max(maxLength, i-start)
                start = lastFound[s[i]] + 1
            lastFound[s[i]] = i 

        return max(maxLength, i-start+1)