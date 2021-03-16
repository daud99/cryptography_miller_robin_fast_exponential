import math

def fastExponential(a, b, c):

    '''
    Calculating a ^ b (mod c)
    :param a:
    :param b:
    :param c:
    :return:
    '''
    power = int(math.log(b, 2))
    if not(2**power == b):
        print("Successive Square method cannot be used as B is not the power of 2\n")
        return

    tmp = a**(2**0) % c
    i = 1
    x = 1
    while(x < b):
        y = ((tmp % c) * (tmp % c)) % c
        tmp = y
        x = 2 ** i
        i = i + 1

    print(f'The {a} ^ {b} mod {c} = {y}')


if "__main__" == __name__:
    fastExponential(7, 256, 13)
    fastExponential(3, 128, 7)



