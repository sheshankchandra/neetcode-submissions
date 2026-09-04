class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0;
        r = len(nums)-1;

        while(nums[l]<=target and l<r):
            mid = l + (r - l) // 2

            if(nums[mid] < target):
                l = mid+1;
            else:
                r = mid;

        if(nums[l] == target):
            return l;

        return -1;