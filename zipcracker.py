from zipfile import ZipFile
import time

start = time.time()
myzip = ZipFile('secret.zip')
base = ''
for i in range(0, 1000000):
    if i < 10:
        base = '00000' + str(i)
    elif i < 100:
        base = '0000' + str(i)
    elif i < 1000:
        base = '000' + str(i)
    elif i < 10000:
        base = '00' + str(i)
    elif i < 100000:
        base = '0' + str(i)
    elif i < 1000000:
        base = str(i)
    try:
        myzip.extractall(pwd=bytes(base, 'utf-8'))
        break
    except:
        1 + 1
print(base)
print(time.time() - start)
