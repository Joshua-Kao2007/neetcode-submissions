import heapq
from typing import List


def get_min_element(arr: List[int]) -> int:
    heap = []
    for num in arr:
        if len(heap) >= 1 and num < -1*heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, -1*num)
        elif len(heap) < 1:
            heapq.heappush(heap, -1*num)
    return -heap[0]

def get_min_4_elements(arr: List[int]) -> List[int]:
    heap = []
    for num in arr:
        if len(heap) >= 4 and num < -1*heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, -1*num)
        elif len(heap) < 4:
            heapq.heappush(heap, -1*num)
    return sorted([-1*val for val in heap])


def get_min_2_elements(arr: List[int]) -> List[int]:
    heap = []
    for num in arr:
        if len(heap) >= 2 and num < -1*heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap,-1* num)
        elif len(heap) < 2:
            heapq.heappush(heap, -1*num)
    return sorted([-1*val for val in heap], reverse=True)


# do not modify below this line
print(get_min_element([1, 2, 3]))
print(get_min_element([3, 2, 1, 4, 6, 2]))
print(get_min_element([1, 9, 7, 3, 2, 1, 4, 6, 2]))

print(get_min_4_elements([1, 9, 7, 3, 2, 1, 4, 6, 2]))
print(get_min_4_elements([1, 9, 7, 2, 1, 3, 2, 1, 4, 6, 2, 1]))
print(get_min_4_elements([1, 9, 7, 2, 3, 2, 4, 6, 2]))

print(get_min_2_elements([1, 9, 7, 3, 2, 1, 4, 6, 2]))
print(get_min_2_elements([1, 9, 7, 2, 1, 3, 2, 1, 4, 6, 2, 1]))
print(get_min_2_elements([1, 9, 7, 2, 3, 2, 4, 6, 2]))

