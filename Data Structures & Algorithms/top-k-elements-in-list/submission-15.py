import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_heap = []
        res = defaultdict(int)
        for num in nums:
            res[num] += 1

        for num,freq in res.items():
            heapq.heappush(my_heap, (-1*freq,num))
        print(my_heap)
        output = []
        for i in range(k):
            output.append(heapq.heappop(my_heap)[1])
        return output