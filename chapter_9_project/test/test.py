# Importing unittest package
import sys
import unittest

from chapter_9_project.solution.UserDefinedException import EmailNotValidError
from chapter_9_project.solution.validate_email_utils import is_email_valid
from chapter_9_project.solution.validate_email_utils_extended import is_email_valid_extended
from chapter_9_project.solution.validate_email_utils_extended_finally import is_email_valid_extended_finally
from chapter_9_project.solution.validate_email_utils_optional_part1 import is_email_valid_optional_regex
from chapter_9_project.solution.validate_email_utils_optional_part2 import is_provider_valid_blacklist_optional

sys.path.append("../")

updated_mailing_list = dict({
    '41c30786-aa84-4d60-9879-0c53f8fad970': ['cgoodleyh', 'ccowlinj@hp.com', 'active'],
    '480fb04a-d7cd-47c5-8079-b580cb14b4d9': ['csheraton4', 'pgatherell6-1.com', 'active'],
    '055dff79-7d09-4194-95f2-48dd586b8bd7': ['mknapton8', 'vlewndenh@spiegel.de', 'active'],
    '9e8fb253-d80d-47b5-8e1d-9a89b5bcc41b': ['paspling7', 'dandersen9@mozilla.org', 'active'],
    '68a32cae-847a-47c5-a77c-0d14ccf11e70': ['tdelicate1', 'hpatel3@springer.com', 'active']})

updated_mailing_list_length = 4
updated_mailing_list_with_valid_providers = 3


class TestValidEmailExceptionHandling(unittest.TestCase):

    def test_email_not_valid_exception(self):
        """
            This function tests the results of the `is_email_valid` function. This unit test checks whether
            the `is_valid_email` raises a user-defined (EmailNotValidError) exception.

            Example:
                is_email_valid(updated_mailing_list)

                This function call must raises an EmailNotValidError exception.

        :return: N/A
        """

        # Check if the result matches the expected output
        with self.assertRaises(EmailNotValidError):
            # Calling the target function and caching the result
            is_email_valid(updated_mailing_list)

    def test_email_not_valid_exception_extended(self):
        """
           This function tests the results of the `is_email_valid_extended` function. This is an extended version
           of the previous unit test. This test checks if the EmailNotValidError exception is handled by the
           `is_email_valid_extended` function.


           Example:
                is_email_valid_extended(updated_mailing_list)

                This function call must return a string with a message handling the exception.

        :return: N/A
        """

        # Calling the target function and caching the result
        result = is_email_valid_extended(updated_mailing_list)

        # Check if the result matches the expected output
        self.assertIsInstance(result, str)

    def test_email_not_valid_exception_finally(self):
        """
           This function tests the results of the `is_email_valid_extended_finally` function. This function extends
           the `is_email_valid_extended` to add the `finally block`. The finally block is responsible to return the
           mailing list after filtering.

           Example:
                is_email_valid_extended_finally(updated_mailing_list)

                This function call must return a list of length 4 with the filtered mailing list.

        :return: N/A
        """

        # Calling the target function and caching the result
        result = len(is_email_valid_extended_finally(updated_mailing_list))

        # Check if the result matches the expected output
        self.assertEqual(result, updated_mailing_list_length)

    def test_email_not_valid_optional_regex(self):
        """
            This function tests the results of the `is_email_valid_optional_regex` function. This function extends
           the `is_email_valid_extended_finally` to add a regex validation. The finally block is responsible to return
           the mailing list after filtering.

           Example:
                is_email_valid_optional_regex(updated_mailing_list)

                This function call must return a list of length 4 with the filtered mailing list.

        :return: N/A
        """

        # Calling the target function and caching the result
        result = len(is_email_valid_optional_regex(updated_mailing_list))

        # Check if the result matches the expected output
        self.assertEqual(result, updated_mailing_list_length)

    def test_provider_valid_blacklist_optional(self):
        """
            TODO

           Example:
                is_email_valid_optional_regex(updated_mailing_list)

                This function call must return a list of length 3 with the filtered mailing list.

        :return: N/A
        """

        # Calling the target function and caching the result
        result = len(is_provider_valid_blacklist_optional(updated_mailing_list))

        self.assertEqual(result, updated_mailing_list_with_valid_providers)

    # def test_provider_valid_blacklist_exception_optional(self):
    #     """
    #         TODO
    #
    #        Example:
    #             is_email_valid_optional_regex(updated_mailing_list)
    #
    #             This function call must return a list of length 3 with the filtered mailing list.
    #
    #     :return: N/A
    #     """
    #
    #     # Check if the result matches the expected output
    #     with self.assertRaises(BlackListProviderException):
    #         # Calling the target function and caching the result
    #         is_provider_valid_blacklist_optional(updated_mailing_list)


if __name__ == '__main__':
    unittest.main()
