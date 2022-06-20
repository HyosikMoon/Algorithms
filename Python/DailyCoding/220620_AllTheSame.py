from typing import List, Any

def all_the_same(elements: List[Any]) -> bool:
    # Initial condtion
    if len(elements) <= 1: return True

    last = elements.pop()
    for _ in range(len(elements)):
        if last == elements.pop(): continue
        else: return False

    return True

print(all_the_same([1, 1, 1]))