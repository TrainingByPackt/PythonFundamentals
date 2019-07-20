## **Chapter 4 - Functions**
This folder contains the artifacts for the chapter 4 of the the "Python Fundamentals" book. This chapter involves 
the creation of a code challenge about **functions**. 

For this code challenge, there is a basic and an extended exercise. A basic exercise will test the student's ability
to work with functions, parameters, return statement, local and global variables.

A more detailed document for this project can be found [here](https://docs.google.com/document/d/1IXZSLZMVXzdgJ-mOFpOp0MKEcT_mu1SaKDDBxuIAG2k/edit?usp=sharing).

## **Project Description**
Develop a functionality to calculate the return on investment for an invest app. The standard gain margin is 0.001% per month, plus 1% each time the amount surpasses 1 million dollars. For example:

If the amount invested is 5000000 (five million dollars), then the gain margin would be:
0.001% + 5%.

Note: AppInvest is a fictitious investment software company especially created for the purpose of this code challenge.
                                                  
    
**Example:**

**Input :** 

```

  calculate_gains(amount_inv=2000000)
  
```

**Output:**

```

2002040.0 # the amount invested plus the gains.

```

                                  
The solution code for this challenge can be found [here](https://github.com/luizhenriqueds/packt-courseware/blob/master/projects/chapter-4/functions.py).

## **Take home extension**
Another anticipated functionality for the app is the ability to estimate the return on investment over a period of time. In order to implement this feature, you will have to update the investment calculator algorithm. The base function to calculate the return on investment from Task 1 can be reutilized here to simplify our task and make use of a very popular strategy in software development in real-life: code reuse.  

This feature will take into consideration a maximum of 1-year period by default, and an extension will be added to the software in the future. 

To calculate the total amount earned over a period of time, you will have to loop through the n-months period (let's keep 12 months for this exercise), and accumulate the gains for each month-period. The other rules from the previous task apply here as well.

**To summarize:**
- Loop over a period of 12 months to calculate the return on investment for each period
- Calculate the gains for each month and store it in a variable
- Accumulate the gains for all the months 
- Return the accumulated estimated value for a period of 12 months


**Hint:** Note that to calculate the accumulated value over a 12-month period is not just multiply the gain of every month
by 12 (or N). In this case, the gain of every month is added to the original value, updating the amount to be invested
in the subsequent month.

The solution code for the extended challenge can be found [here](https://github.com/luizhenriqueds/packt-courseware/blob/master/projects/chapter-4/functions_extended.py).

## **Optional exercise**
As the algorithm performs division of numbers with high precision, it is very common to see really big numbers after
the period (for example: 1200.2300001), which is not desirable because of some reasons: 1. may cause confusion to some
users when they see such big numbers; 2. uses more memory to store a bigger number, and 3. it just does not make
sense to display currency number in this format. 

For this reason, in this bonus project you are going to implement a utility function to format any number into the
appropriate currency format, using 2 decimal places. Also, the function should be able to receive a parameter with the 
desired country code to convert the monetary information. A currency country code is a standardized 3-digit code that 
every country possesses. A list of the all the codes can be found here.

For example: 
The number 1200.2300001 would be became: 1200.23 USD (for United States Dollar).

**Hint:** Take a look at the formatting options for python native.



The solution code for the optional challenge can be found [here](https://github.com/luizhenriqueds/packt-courseware/blob/master/projects/chapter-4/functions_optional.py).

## **Unit Testing**

To run the tests, just execute the test.py file in our preferred IDE. To run tests separately, select the test you
wish to run, click the right button, then "Run Unittests in test.py" in pycharm. 

To run the test from command line, cd into the project's folder, then run the command: ``python test.py``.

The unit test for the code challenges can be found [here](https://github.com/luizhenriqueds/packt-courseware/blob/master/projects/chapter-4/test.py).
