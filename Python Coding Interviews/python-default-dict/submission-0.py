from collections import defaultdict
from typing import List, Dict


def count_chars(s: str) -> Dict[str, int]:
    li = defaultdict(int)
    for let in s:
        li[let] += 1
    return li


def nested_list_to_dict(nums: List[List[int]]) -> Dict[int, List[int]]:
    li = defaultdict(list)
    for element in nums:
        for idx,num in enumerate(element):
            if idx!= 0:
                li[element[0]].append(num)
    return li


# do not modify below this line
print(count_chars("hello"))
print(count_chars("helloworld"))
print(count_chars("areallylongstringwhyareyoureadingthishahalol"))

print(nested_list_to_dict([[1, 2, 3], [4, 5, 6], [1, 4]]))
print(nested_list_to_dict([[1, 2, 3, 4], [4, 5, 6, 7], [1, 4, 5, 6]]))
print(nested_list_to_dict([[5, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]))
print(nested_list_to_dict([[3, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8]]))
