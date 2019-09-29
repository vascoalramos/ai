import math

impar = lambda x: x % 2 != 0
print(f"ímpar: {impar(3)}")


positivo = lambda x: x > 0
print(f"positivo: {positivo(-1)}")


comparacao = lambda x, y: abs(x) < abs(y)
print(f"comparacao: {comparacao(-1, -10)}")


polar_coord = lambda x, y: (math.sqrt(x*x + y*y), math.atan2(y, x))
print(f"coordenadas polares: {polar_coord(2,3)}")


def ex4_5(f, g, h):
    return lambda x, y, z: h(f(x, y), g(y, z))

soma = lambda x, y: x + y
multiplicacao = lambda x, y: x * y
subtracao = lambda x, y: x - y
print(f"function with functions: {ex4_5(soma(2,3), multiplicacao(3,4), subtracao(1,2))}")


universal_quantifier = lambda lst, function: all(function(e) for e in lst)
'''
##### Alternatives:
def quantificador_universal(l,f):
    return not False in [f(e) for e in l]

def quantificador_universal(l,f):
    return l == [e for e in l if f(e)]
'''
print(f"universal_quantifier: {universal_quantifier([-1,2,3,4], lambda x: x > 0)}")


existential_quantifier = lambda lst, function: any(function(e) for e in lst)
print(f"existential_quantifier: {existential_quantifier([-1,-2,-3,4], lambda x: x > 0)}")


is_subset = lambda lst1, lst2: all(e in lst2 for e in lst1)
print(f"is_subset: {is_subset([1,2,3,'a'], [2,3,4,5,10,1,'a'])}")


custom_min = lambda lst, function: min(lst, key=function)
print(f"custom_min: {custom_min(['ol','adeus','aa','b'], lambda x: len(x))}")