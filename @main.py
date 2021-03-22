import utils
import poly
import prime_test
import factorization

# --------------------------------------------------- #
#                        Lab 1                        #
# --------------------------------------------------- #

# print(f"@--Common---@")
# print(f"(GCD), (256, 384): {utils.gcd(256, 384)}")
# print(f"(GCD), (714, 218): {utils.gcd(714, 218)}")
# print(f"(GCD), (516, 438): {utils.gcd(516, 438)}")
# print(f"(GCD), (735, 525): {utils.gcd(735, 525)}")

# print()
# print(f"(Euler), n=63: {utils.euler(63)}")
# print(f"(Euler), n=100: {utils.euler(100)}")
# print(f"(Euler), n=525: {utils.euler(525)}")
# print(f"(Euler), n=31: {utils.euler(31)}")
# print(f"(Euler), n=274: {utils.euler(274)}")

# print()
# print(f"(Primitive roots), n=7: {utils.primitime_roots(7)}")
# print(f"(Primitive roots), n=11: {utils.primitime_roots(11)}")
# print(f"(Primitive roots), n=13: {utils.primitime_roots(13)}")
# print(f"(Primitive roots), n=19: {utils.primitime_roots(19)}")
# print(f"(Primitive roots), n=23: {utils.primitime_roots(23)}")

# print()
# print(f"(Diophantine), 5x+7y=14: {utils.diophantine(5, 7, 14)}")
# print(f"(Diophantine), 27x+36y=32: {utils.diophantine(27, 36, 32)}")
# print(f"(Diophantine), 10x+12y=13: {utils.diophantine(10, 12, 13)}")
# print(f"(Diophantine), 54x+48y=128: {utils.diophantine(54, 48, 128)}")
# print(f"(Diophantine), 14x+27y=49: {utils.diophantine(14, 27, 49)}")
# print(f"(Diophantine), 150x+75y=216: {utils.diophantine(150, 75, 216)}")
# print(f"(Diophantine), 18x+35y=36: {utils.diophantine(18, 35, 36)}")
# print(f"(Diophantine), 50x+44y=121: {utils.diophantine(50, 44, 121)}")

# print()
# print(f"(Comparison), 3x=19 mod 34: {utils.comparison(3, 19, 34)}")
# print(f"(Comparison), 15x=35 mod 100: {utils.comparison(15, 35, 100)}")
# print(f"(Comparison), 16x=19 mod 34: {utils.comparison(16, 19, 34)}")
# print(f"(Comparison), 4x=3 mod 7: {utils.comparison(4, 3, 7)}")
# print(f"(Comparison), 7x=11 mod 39: {utils.comparison(7, 11, 39)}")
# print(f"(Comparison), 9x=21 mod 48: {utils.comparison(9, 21, 48)}")
# print(f"(Comparison), 22x=11 mod 38: {utils.comparison(22, 11, 38)}")
# print(f"(Comparison), 11x=5 mod 17: {utils.comparison(11, 5, 17)}")
# print(f"(Comparison), 5x=8 mod 21: {utils.comparison(5, 8, 21)}")
# print(f"(Comparison), 14x=8 mod 50: {utils.comparison(14, 8, 50)}")
# print(f"(Comparison), 6x=7 mod 22: {utils.comparison(6, 7, 22)}")
# print(f"(Comparison), 2x=5 mod 11: {utils.comparison(2, 5, 1)}")



# --------------------------------------------------- #
#                        Lab 2                        #
# --------------------------------------------------- #

# print()
# print(f"@--Poly---@")
# print(f"1011   * 11  = {poly.mult('1011',   '11')}")
# print(f"101    * 11  = {poly.mult('101',    '11')}")
# print(f"1101   * 101 = {poly.mult('1101',   '101')}")
# print(f"10101  * 111 = {poly.mult('10101',  '111')}")
# print(f"10111  * 11  = {poly.mult('10111',  '11')}")
# print(f"101101 * 111 = {poly.mult('101101', '111')}")

# print()
# print(f"1011   / 11  = {poly.div('1011',   '11')}")
# print(f"101    / 11  = {poly.div('101',    '11')}")
# print(f"1101   / 101 = {poly.div('1101',   '101')}")
# print(f"10101  / 111 = {poly.div('10101',  '111')}")
# print(f"10111  / 11  = {poly.div('10111',  '11')}")
# print(f"101101 / 111 = {poly.div('101101', '111')}")

# print()
# print(f"НОД(100001, 1111)   = {poly.gcd('100001', '1111')}")
# print(f"НОД(110001, 11011)  = {poly.gcd('110001', '11011')}")
# print(f"НОД(10001,  101101) = {poly.gcd('10001',  '101101')}")
# print(f"НОД(111010, 101110) = {poly.gcd('111010', '101110')}")

print(f"НОД(111010, 101110) = {prime_test.original_test(51)}")



# --------------------------------------------------- #
#                        Lab 3                        #
# --------------------------------------------------- #



# --------------------------------------------------- #
#                        Lab 4                        #
# --------------------------------------------------- #

# print()
# print(f"@--Prime Tests---@")
# print(f"(Square root), n=23: {prime_test.square_root_test(23)}")
# print(f"(Square root), n=41: {prime_test.square_root_test(41)}")
# print(f"(Square root), n=15: {prime_test.square_root_test(15)}")
# print(f"(Square root), n=35: {prime_test.square_root_test(35)}")
# print(f"(Square root), n=561: {prime_test.square_root_test(561)}")

# print()
# print(f"(Fermat), n=23: {prime_test.fermat_test(23)}")
# print(f"(Fermat), n=41: {prime_test.fermat_test(41)}")
# print(f"(Fermat), n=15: {prime_test.fermat_test(15)}")
# print(f"(Fermat), n=35: {prime_test.fermat_test(35)}")
# print(f"(Fermat), n=561: {prime_test.fermat_test(561)}")

# print()
# print(f"(Miller-Rabin), n=23: {prime_test.miller_rabin_test(23)}")
# print(f"(Miller-Rabin), n=41: {prime_test.miller_rabin_test(41)}")
# print(f"(Miller-Rabin), n=15: {prime_test.miller_rabin_test(15)}")
# print(f"(Miller-Rabin), n=35: {prime_test.miller_rabin_test(35)}")
# print(f"(Miller-Rabin), n=561: {prime_test.miller_rabin_test(561)}")


# print()
# print(f"@--Factorization---@")
print(f"(Origin), n=483: {factorization.original(483)}")
print(f"(Origin), n=1207: {factorization.original(1207)}")
print(f"(Origin), n=561: {factorization.original(561)}")
print(f"(Origin), n=1219: {factorization.original(1219)}")

print(f"(P-1), n=483: {factorization.pollard_p_minus_one(483)}")
print(f"(P-1), n=1207: {factorization.pollard_p_minus_one(1207)}")
print(f"(P-1), n=561: {factorization.pollard_p_minus_one(561)}")
print(f"(P-1), n=1219: {factorization.pollard_p_minus_one(1219, B=17, M=28, a=2)}")

print()
print(f"(PO), n=483: {factorization.pollard_po(483)}")
print(f"(PO), n=1207: {factorization.pollard_po(1207)}")
print(f"(PO), n=561: {factorization.pollard_po(561)}")
print(f"(PO), n=1219: {factorization.pollard_po(1219)}")

print()
print(f"(Fermat), n=483: {factorization.fermat(483)}")
print(f"(Fermat), n=1207: {factorization.fermat(1207)}")
print(f"(Fermat), n=561: {factorization.fermat(561)}")
print(f"(Fermat), n=1219: {factorization.fermat(1219)}")