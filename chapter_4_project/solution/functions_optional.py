# Importing extended mailing list challenge
import time

from solution.functions_extended import update_mailing_list_extended as ml_updater


def send_message_interval(mailing_list):
    """
         This function contains a unit test to check whether the return of the function `test_send_email_at_interval`
            is correct.

            This function update the mailing list (as the other previous 2), but then simulate an engine to send
            emails to user at a 30 seconds interval. In other words, each user id must be printed after 30 seconds.

    :param mailing_list: the original mailing list with all the users
    :return ids: the list of ids of the active users
    """

    # Array to hold users ids
    ids = []

    # Loop through the mailing list
    for item in ml_updater(mailing_list):
        # Append the resulting ids to the list
        ids.append(item)
        # 30 seconds delay after 'send' the next email
        time.sleep(30)

    # return the list of ids
    return ids
