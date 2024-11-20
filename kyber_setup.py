from sage.all import *

class kyber512():
    def __init__(self, n=256, q=3329):
        # Define the parameters for Kyber from input
        # Note: Defaults are for Kyber512
        self.n = n
        self.q = q

        # Define the rings used in Kyber
        self.R = QuotientRing(PolynomialRing(ZZ, 'x'), x^(self.n) + 1)
        self.Rq = QuotientRing(PolynomialRing(GF(self.q), 'x'), x^(self.n) + 1)

        
