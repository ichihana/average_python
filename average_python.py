import numpy as np
import scipy as sp
from func1 import func1

x = np.array([1,2,3,4,5])
N = len(x)
sum_value = sp.sum(x)
mu = sum_value / N
print(mu)
