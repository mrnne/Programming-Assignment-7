import numpy as np
X= np.random.random((5,5))
x= X.mean()
s= X.std()
Z= (X-x)/s

