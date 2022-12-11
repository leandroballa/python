# import math
from math import hypot

co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
# hyp = math.hypot(co, ca)
hyp = hypot(co, ca)
print('O comprimento da Hipotenusa é {:.2f}'.format(hyp))
