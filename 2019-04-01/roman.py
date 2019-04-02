def int_to_roman(num):
    '''Convert an integer to a Roman numeral string.

    Arguments:
        num (int):
            A non-zero positive integer less than 4000.

    Returns:
        str:
            The Roman numeral representation of ``num``.
    '''
    ONES = ('', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX')
    TENS = ('', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC')
    HUNDREDS = ('', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM')
    THOUSANDS = ('', 'M', 'MM', 'MMM')

    num = int(num)
    assert 0 < num < 4000
    return THOUSANDS[num % 10000 // 1000] + \
           HUNDREDS[num % 1000 // 100] + \
           TENS[num % 100 // 10] + \
           ONES[num % 10]


def test():
    assert int_to_roman(3) == 'III'
    assert int_to_roman(4) == 'IV'
    assert int_to_roman(9) == 'IX'
    assert int_to_roman(58) == 'LVIII'
    assert int_to_roman(1994) == 'MCMXCIV'
    assert int_to_roman(64) == 'LXIV'
    assert int_to_roman(226) == 'CCXXVI'
    assert int_to_roman(900) == 'CM'
    assert int_to_roman(998) == 'CMXCVIII'
    assert int_to_roman(1712 ) == 'MDCCXII'


if __name__ == '__main__':
    test()
