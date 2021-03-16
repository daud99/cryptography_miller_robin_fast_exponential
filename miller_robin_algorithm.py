import random

def millerRobinAlgo(n, s):

    if n == 1:
        print("neither prime nor composite")
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    q = n-1
    k = 0

    while((q % 2) == 0):
        k += 1
        q /= 2

    a = s
    x = (a ** q) % n
    if x == 1 or x == n-1:
        return True

    for j in range(0, k):
        #x = ((((a ** q) % n) ** 2)**j) % n
        x = (x * x) % n
        if (x == n - 1):
            return True
        elif x == 1:
            return False
    return True

if "__main__" == __name__:
    n = int(input("Enter a number to check weather it's an prime or composite: "))
    choice = -1
    s = -1
    all = 0
    while (choice != 1 and choice != 2):
        choice = int(input("Enter 1 to provide specify a possible witness a to test using the Witness procedure or  2 specify a number s of random witnesses for the Miller–Rabin test to check: "))
    if choice == 1:
        while(s < 2 or s > n-2):
            s = int(input("Enter your witness a: "))
            xx = millerRobinAlgo(n, s)
            print(xx)
            if xx == True:
                print("Probably Prime")
            else:
                print("Composite")
    else:
        s = int(input("Enter  number s of random witnesses for the Miller–Rabin test to check: "))
        for _ in range(s):
            if millerRobinAlgo(n, random.randint(2, n-2)) == False:
                print("Composite")
                all = 1
                break
        if all == 0:
            print("Probably Prime")
