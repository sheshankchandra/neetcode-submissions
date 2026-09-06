class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answerList = []
        listOfDict = []

        for obj in strs:
            strDict = {}

            for i in range(len(obj)):
                if obj[i] in strDict:
                    strDict[obj[i]] += 1
                    continue
                strDict[obj[i]] = 1
            
            listOfDict.append(strDict)
            # print(f"appended {strDict} into the listOfDict");

        helperDict = {}

        for i in range(len(listOfDict)):
            sorted_dict = dict(sorted(listOfDict[i].items()))
            sorted_dict_key = str(sorted_dict)
            if sorted_dict_key in helperDict:
                helperDict[sorted_dict_key].append(i)
                # print(f"Found {i} to be as earlier {sorted_dict_key}");
                continue
            helperDict[sorted_dict_key] = [i]
            # print(f"Found {sorted_dict_key} with first index as {i}");

        count = 0;
        for key in helperDict:
            tempList = []
            for val in helperDict[key]:
                tempList.append(strs[val]);
            answerList.append(tempList);                
                
        return answerList;