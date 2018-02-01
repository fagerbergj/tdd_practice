
def closest_prime(x):
    if is_prime(x):
        return x
    mod = 1
    while(True):
        if is_prime(x - mod):
            return x - mod
        if is_prime(x + mod):
            return x + mod
        mod += 1
    return 0
    

def is_prime(x):
    if x == 1 or x == 0:
        return False
    elif x == 2 :
        return True

    if x % 2 == 0:
        return False

    for i in range(3, int(x**.5) + 1, 2):
        if x % i == 0:
            return False
    return True
