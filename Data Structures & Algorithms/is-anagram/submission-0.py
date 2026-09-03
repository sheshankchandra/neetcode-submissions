class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = {};

        for i in s:
            if i in sDict:
                sDict[i] += 1;
                continue;
            sDict[i] = 1;

        for j in t:
            if j in sDict:
                sDict[j] -= 1;
            else:
                return False;
        
        for key in sDict:
            if sDict[key] != 0:
                return False;
        
        return True;
            