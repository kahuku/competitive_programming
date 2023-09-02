# Chick Fil A Intern application summer 2024
# given a number z, return 1 if z can be written as a function p^q of two integers p and q, otherwise return 0

# did not solve this one in time, don't know if this will work or fit within the time constraints (z <= 10^9)
def super_power(z):
    for p in range(2, z):
        for q in range(2, z):
            if p ** q == z:
                return 1
    return 0