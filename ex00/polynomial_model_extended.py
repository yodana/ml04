import numpy as np
def add_polynomial_features(x, power):
    if x.size == 0:
        return None
    empty = np.zeros((x.shape[0], x.shape[1]*power))
    j = 0
    for l in x:
        k = 0
        for i in range(1, power+1):
            for n in l:
                empty[j][k] = n**i
                k = k+ 1
        j = j +1
    return np.array(empty)
x = np.arange(1,11).reshape(5, 2)
x = add_polynomial_features(x, 3)
print(x)
x = np.arange(1,11).reshape(5, 2)
x = add_polynomial_features(x, 4)
print(x)