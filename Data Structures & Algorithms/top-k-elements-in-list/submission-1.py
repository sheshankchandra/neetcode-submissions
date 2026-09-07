import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countDict = {}
        for num in nums:
            if num in countDict:
                countDict[num] += 1
            else:
                countDict[num] = 1

        pq = []
        for key,val in countDict.items():
            heapq.heappush(pq, (-val, key))
        
        ans = []
        while(len(ans) < k and len(pq) != 0):
            val, key = heapq.heappop(pq)
            ans.append(key)
        
        return ans