def head(lst):
    return None if lst == [] else lst[0]


def tail(lst):
    return None if lst == [] else lst[1:]


def join(lst1, lst2):
    if len(lst1) != len(lst2):
        return None
    if lst1 == []:
        return []
    return [(lst1[0], lst2[0])] + join(lst1[1:], lst2[1:])


def min_lst(lst):
    if lst == []:
        return None
    if len(lst) == 1:
        return lst[0]
    min_aux = min_lst(lst[1:])
    return lst[0] if (lst[0] < min_aux) else min_aux


def min_value_and_list(lst): # TODO: dunno
    pass


def min_and_max(lst):
    if lst == []:
        return None
    if len(lst) == 1:
        return (lst[0], lst[0])
    min_aux, max_aux = min_and_max(lst[1:])
    if lst[0] < min_aux:
        min_aux = lst[0]
    if lst[0] > max_aux:
        max_aux = lst[0]
    return (min_aux, max_aux)


def media_mediana(lst): # TODO: later
    pass



if __name__ == "__main__":
    lista1 = [1, 2, 3, 4]
    lista2= [4, 3, 2, 1]
    print(f"head: {head([1,2,3])}")
    print(f"tail: {tail([1,2,3])}")
    print(f"join: {join(lista1, lista2)}")
    print(f"min: {min_lst([1,2,-10,3,-100,-1])}")
    print(f"min value and rest of list:")
    print(f"(min, max): {min_and_max([1,10,2,-10,3,-100,-1,1000])}")
