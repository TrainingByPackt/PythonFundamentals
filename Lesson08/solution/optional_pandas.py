import pandas as pd

# Global variable to set the base path to our dataset folder
base_url = '../dataset/'


def update_mailing_list_pandas(filename):
    """
        This function reads a csv file, filter out rows where `subscribe_status` is not `active` and return the
        number of users with the active flag.

    :param filename: the target filename.
    :return: the number of active users in the original mailing list.
    """

    df = pd.read_csv(base_url + filename)

    return df[df['subscribe_status'] == 'active'].count()[0]
