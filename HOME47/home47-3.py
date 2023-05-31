"""В этой миссии Вам надо определить, все ли элементы массива равны.

Входные: List.

Выходные: Bool."""


from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    # your code here
    l=[]
    for i in elements:
        if i not in l:
            l.append(i)
    
    if len(l) <=1:
        return True
    else:
        return False


print(all_the_same([1, 1, 1]))
print(all_the_same([]))
