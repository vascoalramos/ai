def separar(lst):
    if lst == []:
        return [], []
    a, b = lst[0]
    la, lb = separar(lst[1:])
    return [a]+la, [b]+lb

def remove_e_conta(lst, element):
    if lst == []:
        return [], 0

    lst1, count = remove_e_conta(lst[1:], element)
    if lst[0] == element:
        return lst1, count + 1
    else:
        return [lst[0]] + lst1, count

if __name__ == "__main__":
    lst = [(1,4), (2,3), (3,2), (4,1)]
    print(f"separa: {separar(lst)}")
    print(f"remove e conta: {remove_e_conta([1, 6, 2, 5, 5, 2, 5, 2], 2)}")