from generate_numbers import generate_random_prime
from random import randint
from device import Device

a, b = Device(), Device()

def diffie_hellman_algorithm():
    g = generate_random_prime(max=100)
    n = randint(2, 10 ** 5)

    a.calc_keyg(g, n)
    b.calc_keyg(g, n)

    print(f"g: {g}, n: {n}, ag: {a.keyg}, bg: {b.keyg}")

    a.calc_final_key(b.keyg, n)
    b.calc_final_key(a.keyg, n)


diffie_hellman_algorithm()
