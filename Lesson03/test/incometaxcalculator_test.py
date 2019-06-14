import sys
sys.path.append('../')

from solution.incometaxcalculator_solution import calculate_tax
#from problem.incometaxcalculator import calculate_tax

if __name__ == "__main__":
    assert(calculate_tax(12000, 1, 0) == 11082)
    assert(calculate_tax(20000, 2, 0) == 18470)
    assert(calculate_tax(100000, 1, 1000) == 67815.5)
    print("Well Done!!. All test cases passed.")