class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answerList = []
        helperDict = {}

        for l in range(len(strs)):
            strDict = {}

            for i in range(len(strs[l])):
                if strs[l][i] in strDict:
                    strDict[strs[l][i]] += 1
                    continue
                strDict[strs[l][i]] = 1
            
            sorted_dict = dict(sorted(strDict.items()))
            sorted_dict_key = str(sorted_dict)
            if sorted_dict_key in helperDict:
                helperDict[sorted_dict_key].append(l)
                # print(f"Found {i} to be as earlier {sorted_dict_key}");
                continue
            helperDict[sorted_dict_key] = [l]
            # print(f"Found {sorted_dict_key} with first index as {i}");

        count = 0;
        for key in helperDict:
            tempList = []
            for val in helperDict[key]:
                tempList.append(strs[val]);
            answerList.append(tempList);                
                
        return answerList;