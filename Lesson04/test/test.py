import sys
# Importing unittest package
import unittest

from Lesson04.solution.functions import calculate_gains
from Lesson04.solution.functions_extended import calculate_gains_over_time
from Lesson04.solution.functions_optional import format_currency

sys.path.append("../")


class TestCalculateGains(unittest.TestCase):

    def test_calculate_gains(self) -> None:
        """ This function tests the `calculate_gains` function and checks whether the expected result is returned
        by the function.

        :return: N/A

        """

        result = calculate_gains(2000000)
        expected_result = 2002040.00

        self.assertAlmostEqual(result[0], expected_result, delta=100)

    def test_calculate_gains_over_time(self) -> None:
        """ This function tests the `calculate_gains_over_time` function and checks whether the expected result is
         returned by the function.

        :return: N/A

        """

        result = calculate_gains_over_time(10000, 12)
        expected_result = 10110.66

        self.assertAlmostEqual(result[0], expected_result, delta=100)

    def test_format_currency(self) -> None:
        """ This function tests the `format_currency` function and checks whether the expected result is returned
        by the function.


        :return: N/A

        """

        result = format_currency(100000, 'USD')
        money, currency = result.split()

        expected_result_money = 100000.00
        expected_currency_len = 3

        self.assertEqual(float(money), expected_result_money)
        self.assertEqual(len(currency), expected_currency_len)


if __name__ == '__main__':
    unittest.main()
