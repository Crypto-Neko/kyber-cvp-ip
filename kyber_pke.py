from sage.all import *
from rand_bin import *

class kyber_PKE():
    def __init__(self, n):
        self.n = n

    def keygen(self):
        rho = gen_rand_bin(256)
        sigma = gen_rand_bin(256)

    def encrypt(self, pk, m):
        pass

    def decrypt(self, sk, c):
        pass


