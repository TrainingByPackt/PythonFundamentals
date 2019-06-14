import sys
sys.path.append('../')

from problem.urlvalidator import validate_url
#from solution.urlvalidator_solution import validate_url
if __name__ == "__main__":
    if len(validate_url.__doc__.split()) <= 0:
        print("Please write a docstring describing the function.")
        assert(False)

    assert(validate_url('https://www.technotification.com/2018/06/best-programming-blog.html')==True)
    assert(validate_url('rstp://www.technotification.com/2018/06/best-programming-blog.html')==False)
    assert(validate_url('http://spatialkeydocs.s3.amazonaws.com/FL_insurance_sample.csv')==True)
    assert(validate_url('http://spatialkeydocs.s3.amazonaws.com/FL_insurance_sample/')==False)

    print("Well Done!!. All test cases passed.")