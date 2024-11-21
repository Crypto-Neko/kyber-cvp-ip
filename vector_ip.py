from sage.all import *
from kyber512 import *

'''
Demonstration that integer programming can return a vector in the lattice used in Kyber512.
The program sets up a kyber512 object, uses the definition of Rq as a constraint, and returns
a vector of polynomials in Rq. This will be expanded eventually to returned a vector relevant
to the lattice problem underlying Kyber.
'''

# Define an instance of Kyber
kyber = kyber512()
A = kyber.gen_matrix(kyber.k)
b = kyber.gen_vector(kyber.k)

# Set up the mixed integer linear program solver
mip = MixedIntegerLinearProgram(solver='GLPK')
mip.set_objective(0)

# Define variables for MIP
x_vars = [[mip.new_variable() for _ in range(kyber.n)] for _ in range(kyber.k)]

# Add constraints such that A*x = b
for i in range(kyber.k):
    for j in range(kyber.n):
            expr = sum(A[i, p].coeffs()[j] * x_vars[p][j] for p in range(kyber.k))
            mip.add_constraint(expr == b[i].coeffs()[j] % self.q)        

p.show()
p.solve()


