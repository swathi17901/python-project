
'''
#standard library
import math
print("the value of sqrt is",math.sqrt(49))

#type of import
import math as m
print(m.pi)

#from
from math import pi
print (pi)

#all
from math import *
print("the value is",sqrt(81))
print(pi)
print(tanh)

'''
#user define Modules

import Modules
print(Modules.sub(24,12))


import Modules as m
print(m.add(45,12,1,42))


from Modules import add
print(add(78,45,12,11))

from Modules import *
print(add(45,78,7,5))
greeting("hiiii")









