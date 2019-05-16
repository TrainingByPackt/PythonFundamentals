# Importing re library

# Importing user-defined exceptions
import re

from chapter_9_project.solution.BlackListProviderException import BlackListProviderException


def is_provider_valid_blacklist_optional_len(mailing_list):
    """

        TODO.

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

    # The regex pattern to validate emails
    regex = r"[^@]+@[^@]+\.[^@]+"

    # Loop through the mailing list
    for key, email in mailing_list.items():

        # Check if the @ is present in the email and check if the email passes the regex patter
        if '@' in email[1] and \
                re.match(regex, email[1]):
            # Append the id of users with valid emails

            domains = email[1].split('@')
            providers = domains[1].split('.')[0]

            # Inserted a try.., except.. block to cast the exception
            try:
                # Check if the provider length is greater than 5, which is our condition to consider a provider
                # suspicious.
                if len(providers) >= 5:
                    # Append the id of users with email addresses with valid providers
                    final_users_list.append(key)
            except BlackListProviderException:
                return 'An email in the mailing list is not valid.'
    return final_users_list


def is_provider_valid_blacklist_optional_exception(mailing_list):
    """

        TODO.

        Example:
            '41c30786-aa84-4d60-9879-0c53f8fad970': ['cgoodleyh', 'ccowlinj@hp.com', 'active'],
            '480fb04a-d7cd-47c5-8079-b580cb14b4d9': ['csheraton4', 'pgatherell6-1.com', 'active']

            This should return:
                - '41c30786-aa84-4d60-9879-0c53f8fad970', which is the id of the user with a valid email
                - Print a user-friendly message for the casted exception: 'An email in the mailing list is not valid.'

    :param mailing_list: the current mailing list with the active users
    :return: N/A
    """

    # The regex pattern to validate emails
    regex = r"[^@]+@[^@]+\.[^@]+"

    # Loop through the mailing list
    for key, email in mailing_list.items():

        # Check if the @ is present in the email and check if the email passes the regex patter
        if '@' in email[1] and \
                re.match(regex, email[1]):
            # Append the id of users with valid emails

            domains = email[1].split('@')
            providers = domains[1].split('.')[0]

            # Check if the provider length is greater than 5, which is our condition to consider a provider
            # suspicious.
            if len(providers) < 5:
                # Raises an BlackListProviderException otherwise
                raise BlackListProviderException('Email contains an invalid provider.')
