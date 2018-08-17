import sys
from UserString import MutableString
from string import ascii_uppercase

from numpy import random

from bits.convert_base import BaseConverter


class SpreadsheetEncodingDecoder(BaseConverter):
    alphabet_number_map = {a: p + 1 for p, a in enumerate(ascii_uppercase)}
    number_to_alphabet_map = {v: k for k, v in alphabet_number_map.items()}


def main():
    b1 = 26
    if len(sys.argv) == 2:
        pattern_to_decode = sys.argv[1]
    else:
        number_len = random.randint(1, 6)
        pattern_to_decode = MutableString()
        for _ in range(number_len):
            digit = random.randint(0, 26)
            pattern_to_decode += SpreadsheetEncodingDecoder.number_to_alphabet_map.get(digit, str(digit))
    decoded_pattern = SpreadsheetEncodingDecoder.number_to_decimal(str(pattern_to_decode), b1)
    print('n = %s decoded n = %s' % (pattern_to_decode, decoded_pattern))


if __name__ == '__main__':
    main()
