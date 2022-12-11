from math import sin, cos, tan, radians

ang = float(input('Digite um angulo: '))
seno = sin(radians(ang))
coss = cos(radians(ang))
tang = tan(radians(ang))
print('Para o angulo {}, temos o seno {:.2f}, cosseno {:.2f} e tangente {:.2f}'.format(ang, seno, coss, tang))

