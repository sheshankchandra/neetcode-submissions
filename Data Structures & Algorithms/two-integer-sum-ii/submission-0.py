class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbersInSet = set(numbers)
        ans = [0,0]
        compliment = 0
        found = False

        for i in range(len(numbers)):
            if not found:
                compliment = target - numbers[i]
                if compliment in numbersInSet:
                    ans[0] = i+1
                    found = True
            else:
                if numbers[i] == compliment:
                    ans[1] = i+1
                    return ans;

        return ans;
