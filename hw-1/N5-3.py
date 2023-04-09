import numpy as np
def get_unique_rows(X):
    X_unique = np.unique(X, axis=0)
    return X_unique
X = np.random.randint(4, 6, size=(10,3))
print(X)
print(get_unique_rows(X))