import random


class QBit:
    def __init__(self, value, base):
        self.value = value
        self.base = base

    def read_qbit_from_base(self, read_base):
        if read_base == self.base:
            return self.value
        else:
            return random.getrandbits(1)

    def __repr__(self):
        return f"{self.value =} {self.base =}"

    def __str__(self):
        return f"{self.value =} {self.base =}"


def bb84(n, k):
    # Alice encoding QBits
    a = generate_bits(n)
    a_ = generate_bits(n)
    q_bits = encode_qubits(a, a_)

    # Bob reading QBits from random base
    b_ = generate_bits(n)
    b = decode_qubits(q_bits, b_)

    # Getting indices of unequal base and removing them of both keys
    indices = get_unequal_pairs(a_, b_)
    a_key = remove_bits_at_index(a, indices)
    b_key = remove_bits_at_index(b, indices)

    # Getting random indices to compare
    compare_indices = get_random_indices(k, len(a_key))

    # Getting Bits to compare
    a_compare = get_compare_bits(a_key, compare_indices)
    b_compare = get_compare_bits(b_key, compare_indices)

    # if compare Bits are not equal proceeding is not safe
    if a_compare != b_compare:
        print("Am Kanal wurde gelauscht")
        raise BaseException

    print(f"key of Alice = {a_key}")
    print(f"key of Bob = {b_key}")
    print(f"indices of comparison bits = {compare_indices}")
    print(f"key of Alice without comparison Bits = {remove_bits_at_index(a_key, compare_indices)}")
    print(f"key of Bob without comparison Bits = {remove_bits_at_index(b_key, compare_indices)}")


def get_compare_bits(a, indices):
    tmp = []
    for i in range(len(a)):
        if i in indices:
            tmp.append(a[i])
    return tmp


def get_random_indices(k, length):
    if k > length:
        raise ValueError
    tmp = []
    while len(tmp) != k:
        number = random.randint(0, length-1)
        if number not in tmp:
            tmp.append(number)
    tmp.sort()
    return tmp


def encode_qubits(a, a_):
    if len(a) != len(a_):
        print("Arrays have to be the same length")
        raise ValueError
    tmp = []
    for i, item in enumerate(a):
        tmp.append(QBit(item, a_[i]))
    return tmp


def decode_qubits(a, b_):
    if len(a) != len(b_):
        print("Arrays have to be the same length")
        raise ValueError
    tmp = []
    for i, item in enumerate(a):
        tmp.append(item.read_qbit_from_base(b_[i]))
    return tmp


def generate_bits(n):
    a = []
    for i in range(n):
        a.append(random.getrandbits(1))
    return a


def get_unequal_pairs(a_, b_):
    if len(a_) != len(b_):
        print("Arrays have to be the same length")
        raise ValueError
    tmp = []
    for i in range(len(a_)):
        if a_[i] != b_[i]:
            tmp.append(i)
    return tmp


def remove_bits_at_index(a, indices):
    tmp = []
    for i in range(len(a)):
        if i not in indices:
            tmp.append(a[i])
    return tmp


if __name__ == '__main__':
    bb84(60, 8)
