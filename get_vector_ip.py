from sage.all import *
from kyber512 import *

'''
Demonstration that integer programming can return a vector in the lattice used in Kyber512.
The program sets up a kyber512 object, uses the definition of Rq as a constraint, and returns
a vector of polynomials in Rq. This will be expanded eventually to returned a vector relevant
to the lattice problem underlying Kyber.
'''

kyber = kyber512()

p = MixedIntegerLinearProgram(solver='GLPK')
w = p.new_variable(integer=True, nonnegative=True)
w.add_constraint()
