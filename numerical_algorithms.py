import random
import unittest
import math

from typing import Tuple

def AlKhwarizmiMult(x: int, y: int) -> int:
    """Al-Khwarizmi's method of multiplying two numbers.

    :param x: First number to multiply
    :type x: int
    :param y: Second number to multiply
    :type y: int
    :return: x * y
    :rtype: int
    """
    
    if y == 1:
        return x
    
    if y % 2 == 0:
        return AlKhwarizmiMult(x, y//2) << 1
    else:
        return x + (AlKhwarizmiMult(x, y//2) << 1)

def modularExponentiation(x: int, y: int, N: int) -> int:
    """Compute modular exponentiation, equivalent to x**y mod N

    :param x: base
    :type x: int
    :param y: exponent
    :type y: int
    :param N: modulus
    :type N: int
    :return: x**y mod N
    :rtype: int
    """

    if y == 0:
        return 1
    
    if y % 2 == 0:
        return (modularExponentiation(x, y//2, N)**2) % N
    else:
        return (x * modularExponentiation(x, y//2, N)**2) % N

# Relies on the fact that gcd(x,y) = gcd(x (mod y), y)
def euclidsAlgorithm(x: int, y: int) -> int:
    """Returns the gcd of two numbers x and y.

    :param x: Larger number to return the gcd of
    :type x: int
    :param y: Smaller number to return the gcd of
    :type y: int
    :return: d, gcd of x and y
    :rtype: int
    """
    if y == 0:
        return x
    return euclidsAlgorithm(y, x % y)

def extendedEuclidAlgorithm(x: int, y: int) -> Tuple[int, int, int]:
    """Algorithm that returns both the gcd of two numbers and
    the linear coefficients that can be used to generate it. In other words
    the function returns d,a,b from the equation, d = ax + by.

    :param x: Larger of two numbers to find the gcd of
    :type x: int
    :param y: Smaller of two numbers to find the gcd of
    :type y: int
    :return: d, a, b where d is the gcd and a and b are the linear coefficients
    described above
    :rtype: Tuple[int, int, int]
    """
    if y == 0:
        return (x, 1, 0)
    d, a, b = extendedEuclidAlgorithm(y, x % y)
    return (d, b, a - (x//y) * b)

def fermatsPrimeTest(p: int, k: int = 1) -> bool:
    """Tests if a particular number is prime. This test
    is not perfect as the method uses Fermat's Little Theorem
    and is known to fail for all choices of base for certain numbers,
    (Carmicheal Numbers).

    :param p: Integer to test
    :type p: int
    :param k: Number of bases to draw, increasing k increases accuracy, defaults to 1
    :type k: int, optional
    :return: Returns whether the value p is prime or not
    :rtype: bool
    """
    is_one = True
    for _ in range(k):
        a = random.randint(1, p-1)
        is_one = is_one and (modularExponentiation(a, p-1, p) == 1)
    return is_one

def sieveOfEratosthenes(n: int) -> set:
    """Sieve to return all primes less than a number n.

    :param n: Upper limit to return all primes below, not inclusive.
    :type n: int
    :return: Set of all primes < n.
    :rtype: set
    """
    candidates = set(range(2,n))

    for i in range(2, int(n**(1/2))):
        composite_numbers = set()
        j = 2
        while i * j < n:
            composite_numbers.add(i*j)
            j += 1
        
        candidates -= composite_numbers
    
    return candidates

class RSA:

    def __init__(self, e=3):
        p = self.select_prime()
        q = self.select_prime()
        while q == p:
            q = self.select_prime()
        
        self.p = max(p,q)
        self.q = min(p,q)

        self.e = e
        self.d = self.generate_inverse(e)
    
    def select_prime(self, bits: int = 16) -> int:
        
        is_prime = False
        while not is_prime:
            acc = 0
            for i in range(bits):
                bi = random.randint(0,1)
                acc |= bi
                if i != bits - 1:
                    acc = acc << 1
            is_prime = fermatsPrimeTest(acc)
        return acc
    
    def encrypt_message(self, message: int) -> int:
        return modularExponentiation(message, self.e, self.p*self.q)
    
    def decrypt_message(self, message: int) -> int:
        return modularExponentiation(message, self.d, self.p*self.q)
    
    def generate_inverse(self, e: int) -> int:
        _,d,_ = extendedEuclidAlgorithm(e, self.p-1 * self.q-1)
        return d


class TestNumerical(unittest.TestCase):

    def test_AKM(self):
        x = random.randint(0, 1000)
        y = random.randint(0, 1000)
        self.assertEqual(AlKhwarizmiMult(x,y), x*y)

    def test_modular_exp(self):
        x = random.randint(0, 1000)
        y = random.randint(0, 1000)
        N = random.randint(0, 1000)
        
        self.assertEqual(modularExponentiation(x,y,N), (x**y) % N)
    
    def test_euclids(self):
        x = random.randint(0, 1000)
        y = random.randint(0, 1000)

        if x > y:
            gcd = euclidsAlgorithm(x, y)
        else:
            gcd = euclidsAlgorithm(y, x)

        self.assertEqual(gcd, math.gcd(x,y))

unittest.main()