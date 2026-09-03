class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {};

        for i in range(len(nums)):
            need = target-nums[i];

            if need in numDict:
                return [numDict[need], i];
            numDict[nums[i]] = i;
        
        return [];