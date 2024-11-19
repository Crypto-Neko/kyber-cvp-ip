from sage.all import *
from rand_bin import *

class kyber512_PKE():
    def __init__(self):
        self.n = 256                    # Define the security parameter (dim of poly ring)
        self.k = 3                      # Define the number of secret polys used in keygen
        self.q = 3329                   # Define the order of the ring Z/qZ

        # Define the polynomial ring and the module used for enc and dec
        self.R = PolynomialRing(self.q, self.n)
        self.M = Module(self.R)

    # Generate a key pair (sk, pk) for PKE
    def keygen(self):
        rho = gen_rand_bin(256)
        sigma = gen_rand_bin(256)

    def encrypt(self, pk, m):
        pass

    def decrypt(self, sk, c):
        pass

    # Generate the matrix A from a seed rho
    def gen_matrix(self, rho):
        A = []
        for i in range(self.k):
            row = []
            for j in range(self.k):
                input_data = rho + bytes([i]) + bytes([j])
