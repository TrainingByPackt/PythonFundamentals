import sys
sys.path.append('../')

from solution.incometaxcalculator_solution import calculate_tax
#from problem.incometaxcalculator import calculate_tax
if __name__ == "__main__":
    assert(calculate_tax(1500000, 200000, 150000) == 163800)
    assert(calculate_tax(500000, 200000, 150000) == 0)
    assert(calculate_tax(1000000, 80000, 150000) == 69160)
    print("Well Done!!. All test cases passed.")