import numpy as np
import functools as ft

def fill_list(ls):
    assert len(ls) == 11, "Can't accept blocks larger than 11 bits"

    special_bit_positions = [0, 1, 2, 4, 8]

    block = 16*[0]
    ls_it = 0

    for i, val in enumerate(block):
        if i not in special_bit_positions:
            block[i] = ls[ls_it]
            ls_it += 1;

    print(f"{block} raw")
    return block


def encode16(bits):
    block = fill_list(bits)

    flip_bits = ft.reduce(lambda x, y: x^y, [i for i, bit in enumerate(block) if bit])
    flip_bits = format(flip_bits, 'b')[::-1]

    while len(flip_bits) < 4:
        flip_bits += '0'

    for i, val in enumerate(flip_bits):
        block[2**i] = int(val)




    print(f"{block} encoded")

def main():
    encode16(np.random.randint(0, 2, 11))

if __name__ == "__main__":
    main()
