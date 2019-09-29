import math


def impar(x): return x % 2 != 0


print(f"ímpar: {impar(3)}")


def positivo(x): return x > 0


print(f"positivo: {positivo(-1)}")


def comparacao(x, y): return abs(x) < abs(y)


print(f"comparacao: {comparacao(-1, -10)}")


def polar_coord(x, y): return (math.sqrt(x*x + y*y), math.atan2(y, x))


print(f"coordenadas polares: {polar_coord(2,3)}")


def ex4_5(f, g, h):
    return lambda x, y, z: h(f(x, y), g(y, z))


def soma(x, y): return x + y


def multiplicacao(x, y): return x * y


def subtracao(x, y): return x - y


print(
    f"function with functions: {ex4_5(soma(2,3), multiplicacao(3,4), subtracao(1,2))}")


def universal_quantifier(lst, function): return all(function(e) for e in lst)

'''
##### Alternatives:
def quantificador_universal(l,f):
    return not False in [f(e) for e in l]

def quantificador_universal(l,f):
    return l == [e for e in l if f(e)]
'''
print(
    f"universal_quantifier: {universal_quantifier([-1,2,3,4], lambda x: x > 0)}")


def existential_quantifier(lst, function): return any(function(e) for e in lst)


print(
    f"existential_quantifier: {existential_quantifier([-1,-2,-3,4], lambda x: x > 0)}")


def is_subset(lst1, lst2): return all(e in lst2 for e in lst1)


print(f"is_subset: {is_subset([1,2,3,'a'], [2,3,4,5,10,1,'a'])}")


def custom_min(lst, function): return min(lst, key=function)


print(
    f"custom_min: {custom_min(['ol','adeus','aa','a', 'b'], lambda x: len(x))}")


def min_and_list(lst, function):
    custom_min = min(lst, key=function)
    aux = lst[:]
    aux.remove(custom_min)
    return custom_min, aux


print(
    f"min_and_list: {min_and_list(['ol','adeus','aa','b', 'b'], lambda x: len(x))}")


def mins_and_list(lst, function):
    min_1, min_2 = sorted(lst, key=function)[0:2]
    aux = lst[:]
    aux.remove(min_1)
    aux.remove(min_2)
    return min_1, min_2, aux


print(
    f"mins_and_list: {mins_and_list(['ol','adeus','aa','b', 'a'], lambda x: len(x))}")


def polar_coords(lst):
    return list(map(lambda tup: (math.sqrt(tup[0]*tup[0] + tup[1]*tup[1]), math.atan2(tup[1], tup[0])), lst))


print(f"polar_coords: {polar_coords([(2,3), (3,4), (-1,-1)])}")


def ordered_concat(lst1, lst2, func):
    pass


print("TODO")


def func_concat(lst, func):
    return [func(item) for sublist in lst for item in sublist]


lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(
    f"func_concat: {func_concat(lst, lambda x: x*10)}")


def lists_binary_func(lists, function):
    if len(lists[0]) != len(lists[1]):
        return None
    return list(map(function, lists[0], lists[1]))


lists = ([1, 2, 3, 4], [5, 6, 7, 8])
print(
    f"func_concat: {lists_binary_func(lists, lambda x, y: x+y)}")


def ex_16(): # TODO: nao percebi o que era para fazer
    pass
