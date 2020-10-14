'''
Given a binary number, we are about to do some operations on the number. Two types of operations can be here:

['I', i, j] : Which means invert the bit from i to j (inclusive).

['Q', i] : Answer whether the i'th bit is 0 or 1.

The MSB (most significant bit) is the first bit (i.e. i = 1). The binary number can contain leading zeroes.

Example
binary_simulation("0011001100", [['I', 1, 10], ['I', 2, 7], ['Q', 2], ['Q', 1], ['Q', 7], ['Q', 5]]) === [ '0', '1', '1', '0' ];
binary_simulation("1011110111", [['I', 1, 10], ['I', 2, 7], ['Q', 2], ['Q', 1], ['Q', 7], ['Q', 5]]) === [ '0', '0', '0', '1' ];
binary_simulation("1011110111", [['I', 1, 10], ['I', 2, 7]]) === [];
binary_simulation("0000000000", [['I', 1, 10], ['Q', 2]]) ===  ['1'];
Note
All inputs are valid.
Please optimize your algorithm to avoid time out.
'''


def binary_simulation(s, q):
    out, n, s = [], int(s,2), len(s)
    for t,*i in q:
        if t=='I':
            a,b = i
            n ^= (1<<b-a+1)-1<<(s-b)
        elif t=='Q':
            out.append(str(int(0 < 1<<(s-i[0]) & n)))
    return out
