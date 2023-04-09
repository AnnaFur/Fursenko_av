import numpy as np
a = np.random.randint(-10, 10, size=10)
b = np.random.randint(-10, 10, size=10)
def cal_euclidean(a, b):
    ## Your code here
    c = a - b
    sum_square = np.dot(c, c)
    distance = np.sqrt(sum_square)
    return distance

def cal_manhattan(a, b):
    ## Your code here
    distance = np.linalg.norm(a - b)
    return distance

def cal_cosine(a, b):
    ## Your code here
    cos = (np.dot(a, b)) / ((np.linalg.norm(a)) * (np.linalg.norm(b)))
    distance = 1 - cos
    return distance
print(cal_euclidean(a, b))
print(cal_manhattan(a, b))
print(cal_cosine(a, b))