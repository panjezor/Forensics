import random


class Side:
    def __init__(self, primemodulus, generator):
        self.primemodulus = primemodulus
        self.generator = generator
        self.random = random.randint(1, 20)
        self.public = (self.generator ** self.random) % self.primemodulus

    def addPublic(self, public):
        self.key = (public ** self.random) % self.primemodulus

def checkPrime(number):
    # prime number is always greater than 1
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                return False
                break
        else:
            return True

    # if the entered number is less than or equal to 1
    # then it is not prime number
    else:
        return False


def count(primemodulus, generator):
    if not checkPrime(primemodulus):
        print(str(primemodulus) + " is not a prime number")
    else:
        alice = Side(primemodulus, generator)
        bob = Side(primemodulus, generator)
        alice.addPublic(bob.public)
        bob.addPublic(alice.public)
        print("Prime modulus is equal to " + str(primemodulus))
        print("Generator is equal to " + str(generator))
        print("Alice's random is " + str(alice.random))
        print("Bob's random is " + str(bob.random))
        print("Alice's public is " + str(alice.public) + " and she sends it to Bob")
        print("Bob's public is " + str(bob.public) + " and he sends it to Alice")
        print("Alice's key is " + str(alice.key))
        print("Bob's key is " + str(bob.key))
        if bob.key == alice.key:
            print('everything is fine')


count(7, 4)
