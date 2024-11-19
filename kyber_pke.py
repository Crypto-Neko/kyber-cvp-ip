from sage.all import *
import random as rand

# Generate a random binary string--used in keygen
def gen_rand_bin(n):
    binary = ''
    for i in range (n):
        binary.append(str(rand.randint(0, 1)))
    
    return binary

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


