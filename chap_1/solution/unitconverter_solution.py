import sys

def convert_unit(value, src_unit, dest_unit):
    """Coverts the value in dest_unit from src_unit

    Arguments:
    value -- A positive number.
    src_unit -- string ['kg', 'ounce', 'pound']
    dest_unit -- string ['kg', 'ounce', 'pound']
    
    >>> abs(convert_unit(10.23, 'kg', 'ounce')-360.85302) <= 1e-2
    True
    >>> abs(convert_unit(0.23, 'kg', 'pound')-0.5070626) <= 1e-2
    True
    >>> abs(convert_unit(10.23, 'pound', 'kg')-4.6402554) <= 1e-2
    True
    >>> abs(convert_unit(10.23, 'pound', 'ounce')-163.68) <= 1e-2
    True
    >>> abs(convert_unit(10.23, 'ounce', 'kg')-0.289509) <= 1e-2
    True
    >>> abs(convert_unit(10.23, 'ounce', 'pound')-0.639375) <= 1e-2
    True
    """
    result = -1
    if src_unit == 'kg' and dest_unit == 'pound':
        result = value * 2.20462
    elif src_unit == 'kg' and dest_unit == 'ounce':
        result = value * 35.274
    elif src_unit == 'pound' and dest_unit == 'kg':
        result = value / 2.20462
    elif src_unit == 'pound' and dest_unit == 'ounce':
        result = value * 16
    elif src_unit == 'ounce' and dest_unit == 'kg':
        result = value * 0.0283
    elif src_unit == 'ounce' and dest_unit == 'pound':
        result = value * 0.0625
    elif src_unit == dest_unit:
        result = value
    else:
        print("Please check if src_unit: '{}' and/or dest_unit: '{}' is valid.".format(src_unit, dest_unit) )
    return result

if __name__ == "__main__":
    ## uncommenet the doctest to check correctness of implementation
    """import doctest
    doctest.testmod()"""

    value, src_unit, dest_unit = float(sys.argv[1]), sys.argv[2], sys.argv[4]
    print(value, src_unit, dest_unit)
    print(convert_unit(value, src_unit, dest_unit))


