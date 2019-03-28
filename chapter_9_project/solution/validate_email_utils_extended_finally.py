# Importing user-defined exception
from chapter_9_project.solution.UserDefinedException import EmailNotValidError


def is_email_valid_extended_finally(mailing_list):
    """
        This function extends the previous one by adding a `finally` block to return the user ids for the users
        with valid email addresses.

         Example:
            '41c30786-aa84-4d60-9879-0c53f8fad970': ['cgoodleyh', 'ccowlinj@hp.com', 'active'],
            '480fb04a-d7cd-47c5-8079-b580cb14b4d9': ['csheraton4', 'pgatherell6-1.com', 'active']

            This should return:
                - '41c30786-aa84-4d60-9879-0c53f8fad970', which is the id of the user with a valid email
                - Print a user-friendly message for the casted exception: 'An email in the mailing list is not valid.'


    :param mailing_list: the current mailing list with the active users
    :return: N/A
    """
    # Array to hold user ids
    final_users_list = []

    # Inserted a try.., except.. block to cast the exception
    try:
        # Loop through the mailing list
        for key, email in mailing_list.items():

            # Check if the @ is present in the email
            if '@' in email[1]:
                # Append the id of users with valid emails
                final_users_list.append(key)
        else:

            # Raises an EmailNotValidError otherwise
            raise EmailNotValidError('Email format not valid.')
    except EmailNotValidError:

        # Return a user-friendly message to cast the exception
        print('An email in the mailing list is not valid.')
    finally:

        # Return the id of the users with valid email
        return final_users_list
