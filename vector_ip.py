from sage.all import *
from kyber512 import kyber512

kyber = kyber512()
A = kyber.gen_matrix(kyber.k)
w = [kyber.Rq("x^255"), kyber.Rq("0")]
w = vector(w)
b = A*w
print(b)
print(w)

n = kyber.n
q = kyber.q
k = kyber.k

mip = MixedIntegerLinearProgram(solver='GLPK')
mip.set_objective(0)

x = mip.new_variable(integer=True, nonnegative=True)
z = mip.new_variable(integer=True, nonnegative=True)

x_vars = [[x[m_idx, j] for j in range(n)] for m_idx in range(k)]
z_vars = [[z[i, r] for r in range(n)] for i in range(k)]

for i in range(k):
    # Convert b[i] from field elements to integers
    b_coeffs = [int(c) for c in b[i].list()]
    for r in range(n):
        expr = 0
        for m_idx in range(k):
            Aim_coeffs = A[i,m_idx].list()
            for j in range(n):
                s = (r - j) % n
                sign = -1 if (r - j) < 0 else 1
                expr += int(Aim_coeffs[j]) * x_vars[m_idx][s] * sign
        mip.add_constraint(expr - b_coeffs[r] - q*z_vars[i][r] == 0)

print("About to solve MIP.")
mip.solver_parameter("msg_lev_intopt", 3)
mip.solver_parameter("msg_lev_simplex", 3)
mip.solve()
x_solution = [[mip.get_values(x_vars[m_idx][j]) for j in range(n)] for m_idx in range(k)]

for m_idx in range(k):
    print([int(round(val)) for val in x_solution[m_idx]])

