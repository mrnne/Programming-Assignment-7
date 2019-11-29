import numpy as np
a= np.array([(np.linspace(1,10,10)),(np.linspace(11,20,10)),(np.linspace(21,30,10)),(np.linspace(31,40,10)),(np.linspace(41,50,10)),(np.linspace(51,60,10)),(np.linspace(61,70,10)),(np.linspace(71,80,10)),(np.linspace(81,90,10)),(np.linspace(91,100,10))])
b= np.multiply(a,a)
c= (b[b%3==0])
d= np.int64(c)