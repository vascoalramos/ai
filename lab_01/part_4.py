
impar = lambda x: x % 2 != 0

print(f"ímpar: {impar(3)}")

positivo = lambda x: x > 0

print(f"positivo: {positivo(-1)}")

comparacao = lambda x, y: abs(x) < abs(y)

print(f"comparacao: {comparacao(-1, -10)}")

def ex4_5(f, g, h):
    return lambda x, y, z: h(f(x,y), g(y,z))