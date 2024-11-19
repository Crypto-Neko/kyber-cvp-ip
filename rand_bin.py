import random as rand

# Generate a random binary string--used in keygen
def gen_rand_bin(n):
    binary = ''
    for i in range (n):
        binary.append(str(rand.randint(0, 1)))
    
    return binary
