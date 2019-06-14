## **Chapter 8 - Modules, Packages & Files**
This folder contains the artifacts for the chapter 8 of the the "Python Fundamentals" book. This chapter involves 
the creation of a code challenge about **modules, packages and files**. 

For this code challenge, there is a basic and an extended exercise. A basic exercise will test the student's ability
to work with functions, parameters, iterations, and data structures such as dictionaries with python native.
The extended version will require a little more creativity from the student to take the original problem a little 
further and work with dictionary sorting capabilities. 

A more detailed document for this project can be found [here](#).

## **Project Description**
Extend the chapter 4 project by writing a function that reads the mailing list from a csv file (available in this link) and writes the output to another csv file.

Create a user-defined `mailinglist_validation_util()`  function that receives the following parameters:
Input filename
Output filename
File read/write option

Then make adjustments to the mailing list update function from the functions chapter to save the output into the resulting csv file.

**Example:**

**Input:**

`mailinglist_validation_util('mailing_list.csv', 'updated_mailing_list.csv', 'r+')`

**Output:** 

A csv file of length 5 with the output of the `mailing_list_validation_util` function.

                                  
The solution code for this challenge can be found [here](https://github.com/luizhenriqueds/packt-courseware/blob/master/projects/chapter-8/modules_package_file.py).

## **Take home extension**
You did a great job handling the files for TargetCRM. You were able to read a raw csv file, 
perform some computation on it to filter out unsubscribed users and save the resulting ids back 
to another csv file. Csv files are commonly used file format in many real-world applications and
 knowing how to handle this type of structured persisted data is very useful. 

After the success of your previous implementation, your functionality has been passed in all
 the tests and now it is the time to integrate it to other parts of the CRM application.
 Keep in mind, however, that is not simply just 'plug-in' your implementation to a working software and 
 everything will work properly. Additionally, to avoid mixing your code to an already working code 
 (which could break some functionalities or the tests in the application) you are required to 
 provide a unified way to access your code from external functions.

For this task, you will be required to encapsulate your code and provide an easy access to it 
from the external world. That means that other classes or files of the same project should
 be able to consume your function. In order to do this, save your function into a module called
  `mailinglist_util.py`  and create another file that uses it as a module with the keyword import. 
The solution code for the extended challenge can be found [here](https://github.com/luizhenriqueds/packt-courseware/blob/master/projects/chapter-8/main.py).

## **Bonus Project**

Your implementation is up and running as expected, but as the data grows, TargetCRM needs a way to 
read and write the data in a more efficient way. Other than that, oftenly the manager needs to 
generate reports from the users data, but aggregating values in our architecture right now is very 
resource consuming. 

In order to make a more stable solution to support future demand (taking into account that the data grows
 in a fast pace), you can take advantage of data analysis library solutions available in python. 
 For this bonus project, you will be introduced to a very popular python data analysis package, called Pandas.

Pandas is a very commonly used python resource and has built-in data structures that are very easy to
 work with, such as Series and Dataframes, and several aggregations and analytical functions.

To really stand out in this code delivery, TargetCRM offered you a bonus if you figure out a way to
 implement a more robust and scalable way to read the raw csv data and return the number of users
  in the mailing list. 

## **Below there is a general overview of this bonus project:**
- Install the pandas package 
- Read the csv file into a pandas dataframe
- Filter out the unsubscribed users
- Return the number of active users (the remaining rows)


## **Unit Testing**

To run the tests, just execute the test.py file in your preferred IDE (Pycharm in our case).
To run tests separately, select the test you wish to run, click the right button, 
then "Run Unittests in test.py" in Pycharm.

To run the test from command line, cd into the project's folder, then run the command: ``python test.py``.

The unit test for the code challenges can be found [here](https://github.com/luizhenriqueds/packt-courseware/blob/master/projects/chapter-8/test.py).
