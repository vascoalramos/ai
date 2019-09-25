def list_len(lst):
    if lst == []:
        return 0
    return 1 + list_len(lst[1:])

def sum_list_values(lst):
    if lst == []:
        return 0
    return lst[0] + sum_list_values(lst[1:])

def belongs(element, lst):
    if lst == []:
        return False
    return element == lst[0] or belongs(element, lst[1:])

def concat_lists(lst1, lst2):
    if lst1 == []:
        return lst2
    if lst2 == []:
        return lst1
    
    lst1.append(lst2[0])
    return concat_lists(lst1, lst2[1:])

def inverse_list(lst):
    if lst == []:
        return []
    inv = inverse_list(lst[1:])
    inv[len(inv):] = [lst[0]]
    return inv

def check_capicua(lst): # not yet finished
    if lst == []:
        return True
    

if __name__ == "__main__":
    lst = [1, 2, 3, 4]
    print(f"length: {list_len(lst)}")
    print(f"sum: {sum_list_values(lst)}")
    print(f"belongs: {belongs(5, lst)}")
    print(f"concat: {concat_lists(['w','a','b'], lst)}")
    print(f"inverse: {inverse_list(lst)}")
