from lab_1.gcd import gcd
from lab_1.gcd_extended import gcd_extended
from lab_1.euler import euler
from lab_1.relative_primes import relative_primes
from lab_1.diophantine import diophantine
from lab_1.comparison import comparison
from lab_1.primitive_roots import primitime_roots

def test_gcd():
    print("---Testing gcd---")
    print(f'1, 3: {gcd(1, 3)} = 1')
    print(f'40, 56: {gcd(40, 56)} = 8')
    print(f'33, 28: {gcd(33, 28)} = 1')
    print(f'27, 54: {gcd(27, 54)} = 27')
    print(f'-3, 30: {gcd(-3, 30)} = 3')

def test_gcd_extended():
    pass

def test_euler():
    print("\n---Testing euler---")
    print(f'1: {euler(1)} = 1')
    print(f'2: {euler(2)} = 1')
    print(f'3: {euler(3)} = 2')
    print(f'4: {euler(4)} = 2')
    print(f'5: {euler(5)} = 4')
    print(f'6: {euler(6)} = 2')
    print(f'7: {euler(7)} = 6')
    print(f'8: {euler(8)} = 4')
    print(f'9: {euler(9)} = 6')
    print(f'10: {euler(10)} = 4')

def test_relative_primes():
    pass

def test_diophantine():
    pass

def test_comparison():
    pass

def test_primitive_roots():
    print("\n---Testing primitive roots---")
    print(f'19: {primitime_roots(19)} = [13, 14, 15, 3, 10]')
    print(f'23: {primitime_roots(23)} = [10, 20, 17, 11, 21, 19, 15, 7, 14]')

test_gcd()
test_gcd_extended()
test_euler()
test_relative_primes()
test_diophantine()
test_comparison()
test_primitive_roots()