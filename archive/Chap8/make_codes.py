from PythonLabs.BitLab import Code

from math import ceil, log2

def make_codes(seq):
    n = ceil(log2(len(seq)))
    codes = {}
    for i in range(len(seq)):
        codes[seq[i]] = Code(i, n)
    return codes

