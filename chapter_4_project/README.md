## **Chapter 4 - Functions**
This folder contains the artifacts for the chapter 4 of the the "Python Fundamentals" book. This chapter involves 
the creation of a code challenge about **functions**. 

For this code challenge, there is a basic and an extended exercise. A basic exercise will test the student's ability
to work with functions, parameters, iterations, and data structures such as dictionaries with python native.
The extended version will require a little more creativity from the student to take the original problem a little 
further and work with dictionary sorting capabilities. 

A more detailed document for this project can be found [here](https://docs.google.com/document/d/1IXZSLZMVXzdgJ-mOFpOp0MKEcT_mu1SaKDDBxuIAG2k/edit?usp=sharing).

## **Project Description**
Write a function that reads the mailing list with 15 users provided to you as python dictionary and return the ids of the users that we are able to communicate.

**To update the mailing list, there are some requirements:**
- Remove users that contain the attributes "opt-out", "unsubscribed", or "OPT-OUT" from the list (tip: use str.lower() to transform strings to lowercase)
- The system only sends messages to corporate emails, so filter out 'gmail' users
- Return a list of the users ids that are able to be notified, that is, the remaining users

**This dictionary has the following schema:**

- **uuid**: the user's unique identifier
- **username**: the user's personal nickname
- **email**: the user's email
- **subscribe_status**: the status of a user in the mailing list; the following values are found: 'opt-out', 'OPT-OUT', 'unsubscribed', and 'active '

Consider the following dictionary as our mailing list:


 ```
 mailing_list = dict({'307919e9-d6f0-4ecf-9bef-c1320db8941a': ['afarrimond0', 'thartus0@reuters.com', 'opt-out'],
                     '68a32cae-847a-47c5-a77c-0d14ccf11e70': ['tdelicate1', 'skinmond1@ca.gov', 'opt-out'],
                     '8743d75d-c62a-4bae-8990-3390fefbe5c7': ['edelahuntyk', 'fglossup2@gmail.com', 'OPT-OUT'],
                     'a50bd76f-bc4d-4141-9b5d-3bfb9cb4c65d': ['tdelicate10', 'hpatel3@springer.com', 'active'],
                     '26edd0b3-0040-4ba9-8c19-9b69d565df36': ['ogelder2', 'bissett4@mozilla.org', 'unsubscribed'],
                     '5c96189f-95fe-4638-9753-081a6e1a82e8': ['bnornable3', 'aerrett5@over-blog.com', 'opt-out'],
                     '480fb04a-d7cd-47c5-8079-b580cb14b4d9': ['csheraton4', 'pgatherell6-1.com', 'active'],
                     'd08649ee-62ae-4d1a-b578-fdde309bb721': ['tstodart5', 'schasmoor7@gmail.com', 'active'],
                     '5772c293-c2a9-41ff-a8d3-6c666fc19d9a': ['mbaudino6', 'hpatel3@springer.com', 'unsubscribed'],
                     '9e8fb253-d80d-47b5-8e1d-9a89b5bcc41b': ['paspling7', 'dandersen9@mozilla.org', 'active'],
                     '055dff79-7d09-4194-95f2-48dd586b8bd7': ['mknapton8', 'vlewndenh@spiegel.de', 'active'],
                     '5216dc65-05bb-4aba-a516-3c1317091471': ['ajelf9', 'kmacpaikei@purevolume.com', 'unsubscribed'],
                     '41c30786-aa84-4d60-9879-0c53f8fad970': ['cgoodleyh', 'ccowlinj@hp.com', 'active'],
                     '3fd55224-dbff-4c89-baec-629a3442d8f7': ['smcgonnelli', 'dcarragherk@gmail.com', 'opt-out'],
                     '2ac17a63-a64b-42fc-8780-02c5549f23a7': ['mmayoralj', 'bparsissonl@domainmarket.com',
                                                              'unsubscribed']}) 
                                                              
 ```
                                                              
                                                              
Please, use the provided dict in your project.


**Example:**

**Input :** 

```

  '5216dc65-05bb-4aba-a516-3c1317091471': ['ajelf9', 'kmacpaikei@purevolume.com', 'unsubscribed'],
  '41c30786-aa84-4d60-9879-0c53f8fad970': ['cgoodleyh', 'ccowlinj@hp.com', 'active'],
  '3fd55224-dbff-4c89-baec-629a3442d8f7': ['smcgonnelli', 'dcarragherk@gmail.com', 'active']
  
```

**Output:**

```

['41c30786-aa84-4d60-9879-0c53f8fad970'] # just the id of the user that has not been removed from the mailing list.

```

                                  
The solution code for this challenge can be found [here](https://github.com/luizhenriqueds/packt-courseware/blob/master/projects/chapter-4/functions.py).

## **Take home extension**
**Bellow there is a general overview of this extension project:**
- Update the mailing list or get the user objects from the previous exercise
- Order the list of active users by the username column
- Collect the user ids after sorting the list by username column
- Return the list of active users ids in the same format as the previous exercise

**Tip:** It is a little problematic to work with sorting dictionaries keys by a specific value in python native.
However, there is a very useful utility library to efficiently perform intrinsic operations in python, and it
is called **operator**. The operator module has a very useful **itemgetter** function that is capable of sorting
a list of tuples by the ith element. Consider taking a look at this function.

The solution code for the extended challenge can be found [here](https://github.com/luizhenriqueds/packt-courseware/blob/master/projects/chapter-4/functions_extended.py).

## **Optional exercise**
In order to align the sale of the items being promoted in the email marketing campaign to the other companies' 
call centers, we were asked to implement a more advanced feature. After running your solution for a few months,
they realized that their call center could not keep up the pace to attend several users calling at the same time.
For this reason, they want you to send email campaigns in batches, that is, not all the email would be sent at the
same time, but at small interval instead. They suggested a 30 seconds interval (which is the average time of 
call center attender to do his job) to trigger the emails. Therefore, for the remaining ids, simulate a 
sending engine with the interval of 30 seconds. 

Tip: Just print the user id with a delay of 30 seconds for each id.



The solution code for the optional challenge can be found [here](https://github.com/luizhenriqueds/packt-courseware/blob/master/projects/chapter-4/functions_optional.py).

## **Unit Testing**

To run the tests, just execute the test.py file in our preferred IDE. To run tests separately, select the test you
wish to run, click the right button, then "Run Unittests in test.py" in pycharm. 

To run the test from command line, cd into the project's folder, then run the command: ``python test.py``.

The unit test for the code challenges can be found [here](https://github.com/luizhenriqueds/packt-courseware/blob/master/projects/chapter-4/test.py).
