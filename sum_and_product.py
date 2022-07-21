# Test File for github actions test coverage

def sum(x,y):
    return x + y

def product(x,y):
    return x*y

def main():
    x = 4 
    y = 5
    assert(sum(x,y) == 9)
    assert(product(x,y) == 20)

    print('TESTS PASSED')

main()

