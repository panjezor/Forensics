from zipfile import ZipFile
import time


def checkanother(length, base=''):
    for integ in range(33, 126):
        newbase = base + chr(integ)
        if length > 0:
            try:
                with ZipFile('secret.zip') as zf:
                    zf.extractall(pwd=bytes(newbase, 'utf-8'))
                print(length, newbase)
            except:
                1 + 1
            newl = length - 1
            checkanother(newl, newbase)


def checkall(lengthmax):
    lengthmax += 1
    start = time.time()
    for posslength in range(1, lengthmax):
        print(posslength, time.time() - start)
        checkanother(posslength)


checkall(10)