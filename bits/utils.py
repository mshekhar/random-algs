class BitMixin(object):
    @classmethod
    def set_bit(cls, x, position):
        mask = 1 << position
        return x | mask

    @classmethod
    def clear_bit(cls, x, position):
        mask = 1 << position
        return x & ~mask

    @classmethod
    def flip_bit(cls, x, position):
        mask = 1 << position
        return x ^ mask

    @classmethod
    def is_bit_set(cls, x, position):
        shifted = x >> position
        return shifted & 1

    @classmethod
    def modify_bit(cls, x, position, state):
        """
        One func to modify a bit at a position to a specified state (0 or 1)
        Ex: set bit
        x = 0b00000110
        position = 0b00000101
        state = 0b00000001
        mask = 0b00100000
        ~mask = 0b11011111
        -state = -0b00000001
        x & ~mask = 0b00000110
        -state & mask = 0b00100000
        x & ~mask | -state & mask = 0b00100110

        clear bit
        x = 0b00000110
        position = 0b0000010
        state = 0b00000000
        x & ~mask | -state & mask = 0b00000010
        """
        mask = 1 << position
        return (x & ~mask) | (-state & mask)

    @classmethod
    def is_even(cls, x):
        return (x & 1) == 0

    @classmethod
    def is_power_of_two(cls, x):
        return (x & (x - 1)) == 0
