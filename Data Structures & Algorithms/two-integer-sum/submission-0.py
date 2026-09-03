class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {};
        numSet = set();

        for i in range(len(nums)):
            need = target-nums[i];

            if need in numSet:
                if i > numDict[need]:
                    return [numDict[need], i];
                return [i,numDict[need]];
            else:
                numSet.add(nums[i]);
                numDict[nums[i]] = i;
        
        return [0,0];