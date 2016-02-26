# Additive group mod p is very similar to the multiplicative group mod p with the that:
# 1) the group operation a . b is defined in the following way:
#    a . b := (a + b) % p
#    compare it with the definition of the group operation a . b in multiplicative group mod p:
#    a . b := (a * b) % p
#    pretty similar, right?
# 2) the group contains precisely 1 element more than the multiplicative group:
#    in the additive case G = {0, 1, 2, ... , p - 1}
#    in the multiplicative case G = {1, 2, ... , p - 1}
#    notice the difference in the first element!

# We shall be working with an additive group mod p.
import sys
filenameWithPrime = sys.argv[1]
with open(filenameWithPrime, "r") as f:
    p = int(f.readlines()[0])

# The generator of the group
g = 101

# The result of exponentiation:
a = int(sys.argv[2])

# You're asked to break discrete log in the additive group mod p generated by g, that is, to find x in the following equation: g^x = a.
current = g
counter = 1

# What follows is a BAD way to do this. You need to improve on it using any insights you can get into the structure of G:
while current != a:
    current = (current + g) % p
    counter += 1
print counter