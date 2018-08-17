import random
import sys
from UserString import MutableString


class BaseConverter(object):
    alphabet_number_map = {
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15,
    }
    number_to_alphabet_map = {v: k for k, v in alphabet_number_map.items()}

    @classmethod
    def number_to_decimal(cls, number, base):
        is_neg = number.startswith("-")
        decimal_num = 0
        base_multiplier = 1
        for p, i in enumerate(xrange(len(number) - 1, 0 if is_neg else -1, -1)):
            digit = number[i]
            if p != 0:
                base_multiplier *= base
            if not digit.isdigit():
                transformed_digit = cls.alphabet_number_map[digit]
            else:
                transformed_digit = int(digit)
            decimal_num += transformed_digit * base_multiplier
        return -1 * decimal_num if is_neg else decimal_num

    @classmethod
    def decimal_to_number(cls, number, base):
        converted_num = MutableString()
        is_neg = number < 0
        number = abs(number)
        while number > 0:
            digit = number % base
            converted_num = cls.number_to_alphabet_map.get(digit, str(digit)) + converted_num
            number /= base
        if not converted_num:
            return "0"
        return ("-" if is_neg else "") + converted_num


def main():
    if len(sys.argv) == 4:
        number_to_convert = sys.argv[1]
        b1 = int(sys.argv[2])
        b2 = int(sys.argv[3])
    else:
        number_len = random.randint(1, 16)
        b1 = random.randint(1, 15)
        b2 = random.randint(1, 15)
        number_to_convert = MutableString()
        for _ in range(number_len):
            digit = random.randint(0, b1 - 1)
            number_to_convert += BaseConverter.number_to_alphabet_map.get(digit, str(digit))
    converted_number = BaseConverter.decimal_to_number(BaseConverter.number_to_decimal(str(number_to_convert), b1), b2)
    print('n = %s, base = %d converted n = %s, base - %d' % (number_to_convert, b1, converted_number, b2))


if __name__ == '__main__':
    main()
