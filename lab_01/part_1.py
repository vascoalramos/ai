# function that calculates the length of a list
def list_len(lst):
    if lst == []:
        return 0
    return 1 + list_len(lst[1:])


# function that calculates the sum of all the values in a list
def sum_list_values(lst):
    if lst == []:
        return 0
    return lst[0] + sum_list_values(lst[1:])


# function that validates if a given element belongs to a given list
def belongs(element, lst):
    if lst == []:
        return False
    return element == lst[0] or belongs(element, lst[1:])


# function that concatenates two lists
def concat_lists(lst1, lst2):
    if lst1 == []:
        return lst2
    if lst2 == []:
        return lst1
    lst1.append(lst2[0])
    return concat_lists(lst1, lst2[1:])


# function that returns the inverse of a list
def inverse_list(lst):  # TODO: re-do this one!
    if lst == []:
        return []
    inv = inverse_list(lst[1:])
    inv[len(inv):] = [lst[0]]
    return inv


# function that verifies if a given list is a "capicua"
def check_capicua(lst):
    if lst == []:
        return True
    if lst[0] != lst[-1]:
        return False
    return check_capicua(lst[1:-1])


# function that concatenates a list of lists into a single list
def concat_lists_2(lst):
    pass


# function that return a new list where replaces x by y in a given list
def replace_list(lst, x, y):
    aux = lst[0:1]
    if lst == []:
        return []
    if aux[0] == x:
        aux[0] = y
    return aux + replace_list(lst[1:], x, y)


# function that computes the union of two lists
def union(lst1, lst2):
    if lst1 == []:
        return lst2
    if lst2 == []:
        return lst1
    aux = lst2
    lst1.append(aux[0])
    return union(sorted(lst1), lst2[1:])


# function that given a list return a list with all the sub-sets of the original list
def subsets(lst):
    if lst == []:
        return []
    return [list(range(0, lst[0]+1))] + subsets(lst[1:]) if len(lst) == 1 else [list(range(0, lst[0]))] + subsets(lst[1:])


if __name__ == "__main__":
    lst = [1, 2, 2, 2, 1]
    print(f"length: {list_len(lst)}")
    print(f"sum: {sum_list_values(lst)}")
    print(f"belongs: {belongs(5, lst)}")
    print(f"concat: {concat_lists(['w','a','b'], lst)}")
    print(f"inverse: {inverse_list(lst)}")
    print(f"capicua: {check_capicua(lst)}")
    print(f"concat 2")
    print(f"replace x by y: {replace_list(lst, 1, 10)}")
    print(f"union: {union(lst, [1, 2, 3])}")
    print(f"subsets: {subsets([1, 2, 3])}")
