# Importing user-defined exception
from chapter_9_project.solution.UserDefinedException import EmailNotValidError


def is_email_valid(mailing_list):
    """
        This function validates whether the email addresses in the current mailing list are valid emails.
        To be considered a valid email, for the purpose of the project, we considered any email that contains
        a `@` character.

        Example:
            'pgatherell6-1.com` should raise an EmailNotValidError exception taking into account this email
            does not contain the `@` symbol.


    :param mailing_list: the current mailing list with the active users
    :return: N/A
    """

    # Looping through the mailing list
    for key, email in mailing_list.items():

        # Check if the email contains an @
        if '@' not in email[1]:
            # Raise an EmailNotValidError exception if the @ is not present
            raise EmailNotValidError('Email format not valid.')
