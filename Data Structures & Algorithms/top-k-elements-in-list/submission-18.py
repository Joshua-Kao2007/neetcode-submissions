import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #1 Min Heap
        res = defaultdict(int)
        for num in nums:
            res[num] += 1

        my_heap = []
        for num,freq in res.items():
            heapq.heappush(my_heap, (freq,num))
            if len(my_heap) > k:
                heapq.heappop(my_heap)

        return [num for freq, num in my_heap]
        #2 Bucket Sort
        x = []
        for i in range(len(nums)+1):
            x.append([])
        res = defaultdict(int)
        for num in nums:
            res[num] += 1
        for num,freq in res.items():
            x[freq].append(num)

        res = []
        for i in range(len(x)-1, -1, -1):
            if nums[i]:
                for num in nums[i]:
                    res.append(num)
                    k -= 1
            if k == 0:
                break
        return res




