# Importing unittest package
import unittest

# Importing function from main to test
from chapter_8_project.solution.main import mailing_list_utils_extended as mlu_extended
# Importing the function
from chapter_8_project.solution.modules_package_file import mailinglist_validation_util
from chapter_8_project.solution.optional_pandas import update_mailing_list_pandas

# The output file length, which is the expected output from the tested functions
output_file_length = 5


class TestMailingListFromFile(unittest.TestCase):

    def test_update_mailing_list_from_file(self):
        """
            This function tests the results of the `mailinglist_validation_util` function. It calls the the function
            passing the expected parameters and checks if it matches the expected output.

            Example:
                mailinglist_validation_util('mailing_list.csv', 'output.csv', ['r+', 'w+'])

                This function call must return 5, which is the length of the output file.

        :return: N/A
        """

        # Calling the target function and caching the result
        result = mailinglist_validation_util('mailing_list.csv', 'output.csv', ['r+', 'w+'])

        # Check if the result matches the expected output
        self.assertEqual(result, output_file_length)

    def test_update_mailing_list_from_file_package(self):
        """
            This function tests the results of the `mailinglist_validation_util` function. It calls the the function
            passing the expected parameters and checks if it matches the expected output. The only difference from the
            above function is that this is extended to call the same function from a python package.

            Example:
                mlu.mailinglist_validation_util('mailing_list.csv', 'output.csv', ['r+', 'w+'])
                Where `mlu` is the `mailing_list_utils` package created

                This function call must return 5, which is the length of the output file.

        :return: N/A
        """

        # Calling the target function from a package and caching the result
        # result = mlu.mailinglist_validation_util('mailing_list.csv', 'output.csv', ['r+', 'w+'])
        result = mlu_extended()

        # Check if the result matches the expected output
        self.assertEqual(result, output_file_length)

    def test_update_mailing_list_pandas(self):
        """
            This function tests the output of the `update_mailing_list_pandas` function. The
            `update_mailing_list_pandas` function reads in a csv file, filter only `active` users and return the
            resulting number of rows.

            Example:
                update_mailing_list_pandas('mailing_list.csv')

                This function call must return 6, which is the number of the users with the `active` flag on the
                original mailing list file.

        :return: N/A
        """

        # Calling the target function from a package and caching the result
        # result = mlu.mailinglist_validation_util('mailing_list.csv', 'output.csv', ['r+', 'w+'])
        result = update_mailing_list_pandas('mailing_list.csv')

        # Check if the result matches the expected output
        self.assertEqual(result, (output_file_length + 1))


if __name__ == '__main__':
    unittest.main()
