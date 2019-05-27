# Importing user-defined exception
from chapter_9_project.solution.UserDefinedException import EmailNotValidError


def is_email_valid_extended(mailing_list):
    """
        This function extends the previous by casting the EmailNotValidError exception with a more user-friendly
        message.


        Example:
            'pgatherell6-1.com` should raise an EmailNotValidError exception but return the
            'An email in the mailing list is not valid.' message.

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
        return 'An email in the mailing list is not valid.'
