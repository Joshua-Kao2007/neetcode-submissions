from typing import List

def read_integers() -> List[int]:
    x = input()
    li = [int(i) for i in x.split(",")]
    return li

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
