import datetime
import time

print('Contagem Regressiva!!!')
for x in range(10, 0, -1):
    print(x)
    time.sleep(1)
print('Feliz {}!!!'.format(datetime.date.today().year+1))
