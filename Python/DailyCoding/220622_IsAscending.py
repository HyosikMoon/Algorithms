from typing import Iterable
def is_ascending(items: Iterable[int]) -> bool:
    # initial condition
    if items == []: return True
    
    fst = items[0]
    for i in range(len(items)-1):
        if fst < items[i+1]: continue
        else: return False
    return True