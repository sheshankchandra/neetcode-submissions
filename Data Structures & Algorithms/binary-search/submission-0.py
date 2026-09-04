class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0;
        r = len(nums)-1;

        while(nums[l]<=target and l<r):
            if nums[l]==target:
                return l;

            mid = l+r;
            if(mid%2 != 0):
                mid -= 1
            mid = mid//2

            if(nums[mid] < target):
                l = mid+1;
            else:
                r = mid;

            print(f"l: {l}, r: {r}, mid: {mid}");

        print(nums[l] < target);
        print(l<=r);
        if(nums[l] == target):
            return l;

        return -1;