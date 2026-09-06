class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answerList = []
        helperDict = {}

        for l in range(len(strs)):
            freq = [0] * 26
            curStr = strs[l]

            for i in range(len(curStr)):
                freq[ord(curStr[i]) - ord('a')] += 1

            dictKey = str(freq)
            if dictKey in helperDict:
                helperDict[dictKey].append(strs[l])
                continue
            helperDict[dictKey] = [strs[l]]

        count = 0;
        for key in helperDict:
            tempList = []
            for val in helperDict[key]:
                tempList.append(val);
            answerList.append(tempList);                
                
        return answerList;