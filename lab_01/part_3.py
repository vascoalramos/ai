def join(lst1, lst2):
    if len(lst1) != len(lst2):
        return None
    if lst1 == []:
        return []
    return [(lst1[0], lst2[0])] + join(lst1[1:], lst2[1:])


if __name__ == "__main__":
    lista1 = [1, 2, 3, 4]
    lista2= [4, 3, 2, 1]
    print(f"juntar: {join(lista1, lista2)}")