from sage.all import *
from kyber512 import *

'''
Generates a random x-vector until one lies on the lattice defined in
the Kyber-512 setup. This is a preliminary step to completing the other
problem, which is to generate a lattice point using an MIP solver.
'''

# Define an instance of Kyber
kyber = kyber512()
A = kyber.gen_matrix(kyber.k)
b = kyber.gen_vector(kyber.k)

# Get the initial random value for the vector x
x = kyber.gen_vector(kyber.k)

# Add constraints such that A*x = b
f1 = A[0, 0]
f2 = A[0, 1]
f3 = A[1, 0]
f4 = A[1, 1]
b1 = b[0]
b2 = b[1]

# Loop to check if x is a solution, repeat until is_sol = 1
is_sol = 0
num = 1
while is_sol == 0:
    g1 = x[0]
    g2 = x[1]
    check_1 = (f1*g1 + f2*g2 == b1)
    check_2 = (f3*g1 + f4*g2 == b2)
    if check_1 == check_2 == True:
        is_sol = 1
    if is_sol == 0:
        x = kyber.gen_vector(kyber.k)
        print("Attempt #" + str(num))
        num += 1 

print("Solution found: " + str(x))
