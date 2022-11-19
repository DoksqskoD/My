import itertools
import numpy
X=0
for x in itertools.product('1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM',repeat=8):
    X+=1
    if X%1000000000==0:
        print(str(X/1000000000)+"T")
print(x)