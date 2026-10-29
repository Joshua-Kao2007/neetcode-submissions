from typing import Dict, List # this adds type hints for List and Dict

def get_dict_keys(age_dict: Dict[str, int]) -> List[str]:
    li = []
    for keys in age_dict:
        li.append(keys)
    return li

def get_dict_values(age_dict: Dict[str, int]) -> List[int]:
    li = []
    for k,v in age_dict.items():
        li.append(v)
    return li

# do not modify below this line
dict_1 = {"John": 25, "Doe": 30, "Jane": 22}
dict_2 = {"NeetCode": 24, "NeetCode2": 25, "NeetCode3": 26}

print(get_dict_keys(dict_1))
print(get_dict_keys(dict_2))

print(get_dict_values(dict_1))
print(get_dict_values(dict_2))
