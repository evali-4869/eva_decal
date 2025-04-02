#1 Prime Clusters
import numpy as np

def containsPrimes(arr):
    new_arr = []
    for row in arr:
        for n in row:
            if n > 1:
                for i in range(2, int(n**0.5) + 1):
                    if n % i != 0:
                        new_arr.append(row)
                        break
    return new_arr
print(containsPrimes(np.array([[2, 3, 5], [4, 6, 8], [11, 13, 17], [7, 10, 13]])))

#2.1
def checkerboard():
    board = np.zeros((8,8))
    board[::2, ::2] = 1
    board[1::2, 1::2] = 1
    return board
print(checkerboard())

#2.4
def reverse_checkerboard():
    return 1 - checkerboard()
print(reverse_checkerboard())
                
#3
universe = np.array(["galaxy", "clusters"])

def expansion1(universe):
    return np.array([" ".join(i) for i in universe])
print(expansion1(universe))

def expansion2(universe):
    return np.array(["  ".join(i) for i in universe])
print(expansion2(universe))

#4
np.random.seed(123)
stars = np.random.randint(500, 2000, (5, 5))
def secondDimmest(stars):
    return np.sort(stars)[1]
print(secondDimmest(stars))
        
    