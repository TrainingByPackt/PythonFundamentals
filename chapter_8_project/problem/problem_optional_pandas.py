import pandas as pd

# Global variable to set the base path to our dataset folder
base_url = '../dataset/'


def update_mailing_list_pandas(filename):
    """
       Your docstring documentation starts here.

       For more information on how to proper document your function, please refer to the official PEP8:
        https://www.python.org/dev/peps/pep-0008/#documentation-strings.

    """

    df = # Read your csv file with pandas

    return # Your logic to filter only rows with the `active` flag the return the number of rows

# Calling the function to test your code
print(update_mailing_list_pandas('mailing_list.csv'))
