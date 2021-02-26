from lab_4.ferm_test import ferm_test
from lab_4.miller_rabin_test import miller_rabin_test
from lab_4.square_root_test import square_root_test
from lab_4.ferm_factorization import ferm_factorization
from lab_4.po_pollard_factorization import po_pollard_factorization

def test_ferm_test():
    print("---Testing Ferm Test---\n")
    print(f"n=2: {ferm_test(2, 100)} must be True")
    print(f"n=37: {ferm_test(37, 100)} must be True")
    print(f"n=33: {ferm_test(33, 100)} must be False")
    print(f"n=486: {ferm_test(486, 100)} must be False")
    print(f"n=2345: {ferm_test(2345, 100)} must be False")
    print("\nLABA:")
    print(f"n=23: {ferm_test(23, 100)} must be True")
    print(f"n=41: {ferm_test(41, 100)} must be True")
    print(f"n=15: {ferm_test(15, 100)} must be False")
    print(f"n=35: {ferm_test(35, 100)} must be False")
    print(f"n=561: {ferm_test(561, 100)} must be False")

def test_miller_rabin_test():
    print("---Testing Miller-Rabin Test---\n")
    print(f"n=2: {miller_rabin_test(2, 100)} must be True")
    print(f"n=37: {miller_rabin_test(37, 100)} must be True")
    print(f"n=33: {miller_rabin_test(33, 100)} must be False")
    print(f"n=486: {miller_rabin_test(486, 100)} must be False")
    print(f"n=2345: {miller_rabin_test(2345, 100)} must be False")
    print("\nLABA:")
    print(f"n=23: {miller_rabin_test(23, 100)} must be True")
    print(f"n=41: {miller_rabin_test(41, 100)} must be True")
    print(f"n=15: {miller_rabin_test(15, 100)} must be False")
    print(f"n=35: {miller_rabin_test(35, 100)} must be False")
    print(f"n=561: {miller_rabin_test(561, 100)} must be False")

def test_square_root_test():
    print("---Testing Square Root Test---\n")
    print(f"n=2: {square_root_test(2,)} must be True")
    print(f"n=37: {square_root_test(37)} must be True")
    print(f"n=33: {square_root_test(33)} must be False")
    print(f"n=486: {square_root_test(486)} must be False")
    print(f"n=2345: {square_root_test(2345)} must be False")
    print("\nLABA:")
    print(f"n=23: {square_root_test(23)} must be True")
    print(f"n=41: {square_root_test(41)} must be True")
    print(f"n=15: {square_root_test(15)} must be False")
    print(f"n=35: {square_root_test(35)} must be False")
    print(f"n=561: {square_root_test(561)} must be False")

def test_ferm_factorization():
    print("---Testing ferm factorization---\n")
    print(f"n=517: {ferm_factorization(517)} must be 47*11")
    print(f"n=43: {ferm_factorization(43)} must be 43*1")
    print(f"n=4671: {ferm_factorization(4671)} must be 173*27")
    print(f"n=433: {ferm_factorization(433)} must be 433*1")
    print(f"n=2765: {ferm_factorization(2765)} must be 79*35")
    print("\nLABA:")
    print(f"n=483: {ferm_factorization(483)}")
    print(f"n=1207: {ferm_factorization(1207)}")
    print(f"n=561: {ferm_factorization(561)}")
    print(f"n=1219: {ferm_factorization(1219)}")

def test_po_pollard_factorization():
    print("---Testing PO Pollard factorization---\n")
    print(f"n=517: {po_pollard_factorization(517)} must be 47*11")
    print(f"n=43: {po_pollard_factorization(43)} must be 43*1")
    print(f"n=4671: {po_pollard_factorization(4671)} must be 173*27")
    print(f"n=433: {po_pollard_factorization(433)} must be 433*1")
    print(f"n=2765: {po_pollard_factorization(2765)} must be 79*35")
    print("\nLABA:")
    print(f"n=483: {po_pollard_factorization(483)}")
    print(f"n=1207: {po_pollard_factorization(1207)}")
    print(f"n=561: {po_pollard_factorization(561)}")
    print(f"n=1219: {po_pollard_factorization(1219)}")

# test_ferm_test()
# test_miller_rabin_test()
test_square_root_test()
# test_ferm_factorization()
# test_po_pollard_factorization()