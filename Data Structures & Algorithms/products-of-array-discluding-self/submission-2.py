class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        prefix = [0]*l
        suffix = [0]*l
        pre = 1
        suf = 1       

        for i in range(l):
            pre *= nums[i]
            suf *= nums[l-i-1]
            prefix[i] = pre
            suffix[l-i-1] = suf

        # print(str(prefix))
        # print(str(suffix))
        # [1,2,8,48]
        # [48,48,24,6]

        output = []

        for i in range(l):
            cur = 1
            if i == 0:
                cur *= suffix[i+1]
            elif i == l-1:
                cur *= prefix[i-1]
            else:
                cur = suffix[i+1] * prefix[i-1]
            
            output.append(cur)

        return output