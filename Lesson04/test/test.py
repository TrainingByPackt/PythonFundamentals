import sys
import time
# Importing unittest package
import unittest

# Importing simple mailing list challenge
from Lesson04.solution.functions import update_mailing_list as mailing_list_challenge
# Importing extended mailing list challenge
from Lesson04.solution.functions_extended import update_mailing_list_extended as mailing_list_challenge_ext
from Lesson04.solution.functions_optional import send_message_interval as smi

sys.path.append("../")

# The dictionary with the original mailing list
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


class TestMailingList(unittest.TestCase):

    def test_update_mailing_list(self):
        """
                    This function contains a unit test to check whether the return of the function `update_mailing_list`
                    is correct.

                    Passed a list of user contacts in a CRM database, the function has to filter out those users
                    whose contacts do not have the flag `active` and keep only those with professional email addresses.

                    The function's final output is only the ids of the active users.

                :return: N/A

                """

        result = mailing_list_challenge(mailing_list)

        response = ['a50bd76f-bc4d-4141-9b5d-3bfb9cb4c65d',
                    '480fb04a-d7cd-47c5-8079-b580cb14b4d9',
                    '9e8fb253-d80d-47b5-8e1d-9a89b5bcc41b',
                    '055dff79-7d09-4194-95f2-48dd586b8bd7',
                    '41c30786-aa84-4d60-9879-0c53f8fad970']

        self.assertEqual(result, response)

    def test_update_mailing_list_extended(self):
        """
            This function contains a unit test to check whether the return of the function `update_mailing_list`
            is correct.

            Passed a list of user contacts in a CRM database, the function has to filter out those users whose contacts
            do not have the flag `active` and keep only those with professional email addresses.

            After that, the code has to order the remaining users alphabetically. Additionally, the function's final
            output is only the ids of the active users.

        :return: N/A

        """

        result = mailing_list_challenge_ext(mailing_list)

        response = ['41c30786-aa84-4d60-9879-0c53f8fad970',
                    '480fb04a-d7cd-47c5-8079-b580cb14b4d9',
                    '055dff79-7d09-4194-95f2-48dd586b8bd7',
                    '9e8fb253-d80d-47b5-8e1d-9a89b5bcc41b',
                    'a50bd76f-bc4d-4141-9b5d-3bfb9cb4c65d']

        self.assertEqual(result, response)

    def test_send_email_at_interval(self):
        """
            This function contains a unit test to check whether the return of the function `test_send_email_at_interval`
            is correct.

            This function update the mailing list (as the other previous 2), but then simulate an engine to send
            emails to user at a 30 seconds interval. In other words, each user id must be printed after 30 seconds.

            As we are dealing with floating points (seconds), a 1 second interval will be tolerated.

        :return: N/A

        """

        # Tag the initial time
        start_time = time.time()

        # Call the function
        result = smi(mailing_list)

        # Calculate the elapsed time to simulate the email send at intervals engine
        elapsed_time = time.time() - start_time

        # Expected response
        delay_response = len(result) * 30

        # Accepted tolerance
        deviation = 1

        response = ['41c30786-aa84-4d60-9879-0c53f8fad970',
                    '480fb04a-d7cd-47c5-8079-b580cb14b4d9',
                    '055dff79-7d09-4194-95f2-48dd586b8bd7',
                    '9e8fb253-d80d-47b5-8e1d-9a89b5bcc41b',
                    'a50bd76f-bc4d-4141-9b5d-3bfb9cb4c65d']

        self.assertEqual(set(result), set(response))
        self.assertGreaterEqual(elapsed_time, delay_response)
        self.assertLessEqual(elapsed_time, (delay_response + deviation))


if __name__ == '__main__':
    unittest.main()
