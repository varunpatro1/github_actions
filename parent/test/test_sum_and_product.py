#This file will contain the tests

from parent.proj.sum_and_product import *

def test_get_sum():
    assert(get_sum(4,5) == 9)

def test_get_product():
    assert(get_product(4,5) == 20)

def main():
    print(get_sum(4,5))

main()





