from lab_2.mult import mult
from lab_2.add import add
from lab_2.div import div_core, div
from lab_2.gcd import gcd as polynome_gcd

def test_mult():
    print("---Testing mult---")
    print(f"1101, 101: {mult('1101', '101')} = 111001")

def test_add():
    print("\n---Testing add---")
    print(f"1101, 101: {add('1101', '101')} = 1000")
    print(f"101, 11101: {add('101', '11101')} = 11000")
    print(f"101101, 111: {add('101101', '111')} = 101010")

def test_div():
    print("\n---Testing div---")
    # print(f"1101, 101: {div('1101', '101')} = (11, 10)")
    print(f"1101, 11: {div('1101', '11')} = (11, 0)")

def test_gcd():
    print("\n---Testing gcd---")
    print(f"100001, 1111: {polynome_gcd('100001', '1111')} = 11")

# test_mult()
# test_add()
test_div()
# test_gcd()