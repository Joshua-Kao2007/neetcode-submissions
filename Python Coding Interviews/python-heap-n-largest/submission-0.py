import heapq
from typing import List


def get_max_element(arr: List[int]) -> int:
    heap = []
    for num in arr:
        if len(heap) >= 1 and num > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, num)
        elif len(heap) < 1:
            heapq.heappush(heap, num)
    return heap[0]


def get_max_4_elements(arr: List[int]) -> List[int]:
    # Return elements in *decreasing* order
    heap = []
    for num in arr:
        if len(heap) >= 4 and num > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, num)
        elif len(heap) < 4:
            heapq.heappush(heap, num)
    return sorted([val for val in heap], reverse = True)


def get_max_2_elements(arr: List[int]) -> List[int]:
    # Return elements in *increasing* order
    heap = []
    for num in arr:
        if len(heap) >= 2 and num > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, num)
        elif len(heap) < 2:
            heapq.heappush(heap, num)
    return sorted([val for val in heap])



# do not modify below this line
print(get_max_element([1, 2, 3]))
print(get_max_element([3, 2, 1, 4, 6, 2]))
print(get_max_element([1, 9, 7, 3, 2, 1, 4, 6, 2]))

print(get_max_4_elements([4, 9, 7, 3, 2, 7, 4, 6, 2]))
print(get_max_4_elements([4, 9, 7, 2, 1, 3, 2, 3, 4, 6, 2, 3]))
print(get_max_4_elements([4, 7, 2, 3, 2, 4, 6, 2]))

print(get_max_2_elements([4, 5, 3, 7]))
print(get_max_2_elements([8, 8, 7, 9]))
print(get_max_2_elements([1, 2, 3, 9, 8, 7, 6]))

