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