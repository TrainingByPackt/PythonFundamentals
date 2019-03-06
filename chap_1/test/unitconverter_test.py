import sys
from problem import convert_unit    
if __name__ == "__main__":
    if len(convert_unit.__doc__.split()) <= 0:
        print("Please write a docstring describing the function.")
        assert(False)
    assert(abs(convert_unit(10.23, 'kg', 'ounce')-360.85302) <= 1e-2)
    assert(abs(convert_unit(0.23, 'kg', 'pound')-0.5070626) <= 1e-2)
    assert(abs(convert_unit(10.23, 'pound', 'kg')-4.6402554) <= 1e-2)
    assert(abs(convert_unit(10.23, 'pound', 'ounce')-163.68) <= 1e-2)
    assert(abs(convert_unit(10.23, 'ounce', 'kg')-0.289509) <= 1e-2)
    assert(abs(convert_unit(10.23, 'ounce', 'pound')-0.639375) <= 1e-2)

    print("Well Done!!. All test cases passed.")