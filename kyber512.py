from sage.all import *

class kyber512():
    def __init__(self, n=256, q=3329, k=2):
        # Define the parameters for Kyber from input
        # Note: Defaults are for Kyber512
        self.n = n
        self.q = q
        self.k = k

        # Define the rings used in Kyber
        PRZ = PolynomialRing(ZZ, 'x')
        PRq = PolynomialRing(GF(self.q), 'x')
        self.R = QuotientRing(PRZ, PRZ.gen()**(self.n) + 1)
        self.Rq = QuotientRing(PRq, PRq.gen()**(self.n) + 1)

        # Define the space of matrices from which A is selected
        self.M = MatrixSpace(self.Rq, self.k)

    # Generate a random matrix from self.M
    def gen_matrix(k):
        return self.M([[rand_poly() for _ in range(k)] for _ in range(k)])

    # Generate a random vector of elements in Rq
    def gen_vector(k):
        return [random_polynomial() for _ in range(k)]

    # Generate a random polynomial in self.Rq
    def rand_poly(k):
        return sum([GF(q).random_element() * R.gen()**i for i in range(self.n)])
