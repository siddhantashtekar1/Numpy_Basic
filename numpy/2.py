import numpy as np 

import sys 

import time

# 1.memory test between numpy and list

s=range(1000)

print(sys.getsizeof(5)*len(s))

d=np.arange(1000)

print(d.size*d.itemsize)




# time difference between the numpy and list

size=10000000

l1=range(size)
l2=range(size)

a1=np.arange(size)
a2=np.arange(size)

start=time.time()

result =[(x,y) for x,y in zip(l1,l2)]

print((time.time()-start)*1000)

start=time.time()

result=a1+a2

print((time.time()-start)*1000)