from zipfile import ZipFile
import time

arraychar = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a',
             's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y',
             'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
arraynum = range(0, 10)


def checkanother(length, start, base=''):
    for arraystr in arraynum:
        newbase = base + str(arraystr)
        if length > 0:
            try:
                with ZipFile('secret.zip') as zf:
                    zf.extractall(pwd=bytes(newbase, 'utf-8'))
                print(length, newbase, time.time() - start)
            except:
                 1 + 1
            newl = length - 1
            checkanother(newl, newbase)


def checkall(lengthmax):
    lengthmax += 1
    start = time.time()
    for posslength in range(1, lengthmax):
        print(posslength, time.time() - start)
        checkanother(posslength, start)


checkall(6)