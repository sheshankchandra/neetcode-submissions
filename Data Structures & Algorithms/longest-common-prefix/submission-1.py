class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = 0;
        maxLength = float('-inf')

        while True:
            prefix = strs[0][0:ans+1]
            broke = False
            for i in range(len(strs)):
                if(strs[i][0:ans+1] != prefix):
                    broke = True
                    break
                maxLength = max(maxLength, len(strs[i]))
            
            if broke:
                break
            ans += 1

            if(ans > maxLength):
                ans = maxLength
                break
        
        return strs[0][0:ans]