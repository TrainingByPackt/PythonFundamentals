## **Chapter 9 - Exception Handling**
This folder contains the artifacts for the chapter 9 of the the "Python Fundamentals" book. This chapter involves 
the creation of a code challenge about **exception handling**.

**In this project, the student will apply the following concepts:**

- Create your custom user-defined exception
- Preventing your code to crash with error handling
- Improving user experience with application feedback
- Use advanced real-world pattern filters to evaluate email address format
- Document your functions with PEP8 docstring documentation


A more detailed document for this project can be found [here](https://docs.google.com/document/d/1BNyBfz-n2cddLLw7MbDe4n7PHSxOBI--i1M6-WeFz1I/edit?usp=sharing).

## **Project Description**


In this challenge, you will create a custom exception that is thrown when an invalid email is found. Consider a valid email every email that contains the '@' symbol. 

Create a custom exception EmailNotValidError that will be raised when an email in the mailing list is not valid. 
Below is the updated mailing list that you will work with. 

``` updated_mailing_list = dict({
'41c30786-aa84-4d60-9879-0c53f8fad970': ['cgoodleyh', 'ccowlinj@hp.com', 'active'],
'480fb04a-d7cd-47c5-8079-b580cb14b4d9': ['csheraton4', 'pgatherell6-1.com', 'active'],
'055dff79-7d09-4194-95f2-48dd586b8bd7': ['mknapton8', 'vlewndenh@spiegel.de', 'active'],
'9e8fb253-d80d-47b5-8e1d-9a89b5bcc41b': ['paspling7', 'dandersen9@mozilla.org', 'active'],
'68a32cae-847a-47c5-a77c-0d14ccf11e70': ['tdelicate1', 'hpatel3@springer.com', 'active']})
```

Please, use the provided dict in your project.

In this example, you will validate for each email in the mailing list if it contains an ‘@’ symbol in order to consider that particular email a valid address. A validation example follows.

**Example:** 

**Input:** 

```
'480fb04a-d7cd-47c5-8079-b580cb14b4d9': ['csheraton4', 'pgatherell6-1.com', 'active'],
'5772c293-c2a9-41ff-a8d3-6c666fc19d9a': ['mbaudino6', 'hpatel3-1.com', 'active']
```

**Output:** 
```
An exception of type EmailNotValidError
```

In order to accomplish the tasks for this project, you will need to create a 
custom [user-defined exception](https://github.com/TrainingByPackt/PythonFundamentals/blob/master/chapter_9_project/solution/UserDefinedException.py)
that will be thrown when an invalid email address is found. Next, you will implement improvements to this project 
in order to make it more intuitive to the user such as casting the error and avoiding the program to crash and return
the nicely formatted emails even if there is an exception during the execution. 
                 

The solution code for this challenge can be found [here](https://github.com/TrainingByPackt/PythonFundamentals/blob/master/chapter_9_project/solution/validate_email_utils.py).

## **Take home extension**

Create a function called `is_email_valid_extended()` to cast the exception and prints a message to the user and prevent
the code to crash with an error message. Below is the template code provided to you as a starting point to your
implementation: 



```
# Import user-defined exception

def is_email_valid_extended(mailing_list):
     """
       Your docstring documentation starts here.

       For more information on how to proper document your function, please refer to the official PEP8:
        https://www.python.org/dev/peps/pep-0008/#documentation-strings.

    """


    final_users_list = # Array to hold user ids

    # Inserted a try.., except.. block to cast the exception
    try:

        # Loop through the mailing list
        for key, email in # Your mailing list:


            if '@' in # Check if the @ is present in the email:

                # Append the id of users with valid emails

        else:


            raise # Raises an EmailNotValidError otherwise
    except # Your user-defined exception:


        return # Return a user-friendly message to cast the exception
```

Create a function called `is_email_valid_extended_finally()` that implements the finally block and return the
list of valid emails after all the code executed. A function template code is provided to you below.

```
# Importing user-defined exception


def is_email_valid_extended_finally(mailing_list):
     """
       Your docstring documentation starts here.

       For more information on how to proper document your function, please refer to the official PEP8:
        https://www.python.org/dev/peps/pep-0008/#documentation-strings.

    """

    final_users_list = # Array to hold user ids

    # Inserted a try.., except.. block to cast the exception
    try:
        # Loop through the mailing list
        for key, email in  # Your mailing list:


            if '@' in # Check if the @ is present in the email:

                # Append the id of users with valid emails

        else:


            raise # Raises an EmailNotValidError otherwise
    except # Your user-defined exception:

        # Print a user-friendly message to cast the exception
    finally:

        return # Return the id of the users with valid email
```

The solution code for the extended challenge can be found at the following addresses:
[part 1](https://github.com/TrainingByPackt/PythonFundamentals/blob/master/chapter_9_project/solution/validate_email_utils_extended.py)
and [part 2](https://github.com/TrainingByPackt/PythonFundamentals/blob/master/chapter_9_project/solution/validate_email_utils_extended_finally.py).

## **Optional exercise**


Your proposed solution has been working well for a couple of weeks. After a few iterations, the TargetCRM’s CTO 
collected the mailing list data again to check if the email addresses data quality had increased. 
As expected, number of incorrect emails decreased a lot, and the company is happy with the initial improvements
that your functionality has brought to the platform.

However, after a few weeks of iterations and tests, the CTO realized that much more complicated errors were present 
in the email data, that a simple ‘@’ symbol check was not covering. He then realized the feature was not capturing
the more complex bad format inputs. 

Some bad email formats that were passed in the initial validation:
```
john@gmail
.@email.com
```

The above email addresses had passed our current validation but are still invalid emails. Therefore, to create a more
robust validator, we will need to move on to a more complex technique. For this bonus project, implement a solution
using regex to create a more complex email validator. 

Hint: Python has a built-in library to work with regular expressions called re. Additionally, take a look at
the regular expression pattern to validate email formats. 

This project involves techniques to solve real-world problems such as pattern string matching. So, we encourage
you to take a moment and try to solve it as you will need this ability as a software developer.



The solution code for the optional challenge can be found [here](https://github.com/TrainingByPackt/PythonFundamentals/blob/master/chapter_9_project/solution/validate_email_utils_optional_regex.py).

## **Unit Testing**

To run the tests, just execute the test.py file in our preferred IDE. To run tests separately, select the test you
wish to run, click the right button, then "Run Unittests in test.py" in pycharm. 

To run the test from command line, cd into the project's folder, then run the command: ``python test.py``.

The unit test for the code challenges can be found [here](https://github.com/TrainingByPackt/PythonFundamentals/blob/master/chapter_9_project/test/test.py).
