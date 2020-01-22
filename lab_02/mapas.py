from constraintsearch import *


def mapa_constraint(r1, c1, r2, c2):
    return c1 != c2


def make_constraint_graph(mapa):
    return { (X, Y): mapa_constraint for X in mapa for Y in mapa[X] } 


def make_domains(mapa, cores):
    return { r: cores for r in mapa }


alinea_a = {"A": "BED", "B": "AEC", "C": "BED", "D": "AEC", "E": "ABCD"}

cores = ["vermelho", "verde", "azul", "amarelo" "branco"]

cs = ConstraintSearch(make_domains(alinea_a, cores), make_constraint_graph(alinea_a))

print(cs.search())
print(cs.call)
