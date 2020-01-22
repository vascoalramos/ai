from constraintsearch import *


def amigo_constraint(a1, t1, a2, t2):
    c1, b1 = t1
    c2, b2 = t2

    if a1 in [c1, b1] or a2 in [c2, b2]:
        return False

    if c1 == b1 or c2 == b2:
        return False

    if c1 == "claudio" and b1 != "bernardo":
        return False

    return True


def make_constraint_graph(amigos):
    return {(X, Y): amigo_constraint for X in amigos for Y in amigos}


def make_domains(amigos):
    return {a: [(c, b) for c in amigos for b in amigos] for a in amigos}



amigos = ["andre", "bernardo", "claudio"]

cs = ConstraintSearch(make_domains(amigos), make_constraint_graph(amigos))

solution, call = cs.search()
print(solution)
print(call)
