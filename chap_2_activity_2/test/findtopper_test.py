import sys
sys.path.append('../')

#from solution.findtopper_solution import rank_user
from problem.findtopper import rank_user
if __name__ == "__main__":
    assert(rank_user(['a', 'b', 'c'], [11, 10.1, 12.3]) == {'a':2, 'b':3, 'c':1})
    assert(rank_user(['a', 'b', 'c'], [11, 11, 11]) == {'a':1, 'b':1, 'c':1})
    assert(rank_user(['a', 'b', 'c'], [11.1, 11, 11]) == {'a':1, 'b':2, 'c':2})
    
    print("Well Done!!. All test cases passed.")