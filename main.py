import math
import random


def bb84(n):
    a, a_ = generate_bits(n)
    a = encode_bits(a, a_)


def encode_bits(a, a_):
    for i, item in enumerate(a):
        if a_[i] == 0:
            if item == 1:
                a[i] = complex(0, 1)
            else:
                a[i] = complex(1, 0)
        else:
            pass
            # insert hadamar base here
    return a


def generate_qubits(n):
    a = []
    a_ = []
    for i in range(n):
        a.append(generate_random_qubit())
        a_.append(generate_random_qubit())
    return a, a_


def generate_random_qubit():
    while True:
        try:
            a = complex(random.random(), random.random())
            b = random.random()
            b = complex(b, math.sqrt(1-(abs(a)**2+b**2)))
            return a, b
        except ValueError:
            pass


def hadamar_basis(a):
    pass


def generate_bits(n):
    a = []
    a_ = []
    for i in range(n):
        a.append(random.getrandbits(1))
        a_.append(random.getrandbits(1))
    return a, a_


if __name__ == '__main__':
    print(generate_qubits(100))

