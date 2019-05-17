# Importing re library

# Importing user-defined exceptions
import re

from chapter_9_project.solution.BlackListProviderException import BlackListProviderException


def is_provider_valid_blacklist_optional_len(mailing_list):
    """

        Checks if an email provider is valid or not. If it is on blacklist, the email is removed from list.


    :param mailing_list: the current mailing list with the active users
    :return: updated mailing list
    """

    # Array to hold user ids
    final_users_list = []

    # The regex pattern to validate emails
    regex = r"[^@]+@[^@]+\.[^@]+"

    # Loop through the mailing list
    for key, email in mailing_list.items():

        # Check if the @ is present in the email and check if the email passes the regex pattern
        if '@' in email[1] and \
                re.match(regex, email[1]):
            # Append the id of users with valid emails

            domain = email[1].split('@')
            providers = domain[1].split('.')[0]

            # Inserted a try.., except.. block to cast the exception
            try:
                # Check if the provider length is greater than 5, which is our condition to consider a provider
                # suspicious.
                if len(providers) >= 5:
                    # Append the id of users with email addresses with valid providers
                    final_users_list.append(key)

            except BlackListProviderException:
                return 'An email in the list contains a provider in blacklist.'

    return final_users_list


def is_provider_valid_blacklist_optional_exception(mailing_list):
    """

        Checks if an email provider is valid or not. If it is on blacklist, the email is removed from list.

    :param mailing_list: the current mailing list with the active users
    :return: N/A
    """

    # The regex pattern to validate emails
    regex = r"[^@]+@[^@]+\.[^@]+"

    # Loop through the mailing list
    for key, email in mailing_list.items():

        # Check if the @ is present in the email and check if the email passes the regex pattern
        if '@' in email[1] and \
                re.match(regex, email[1]):
            # Append the id of users with valid emails

            domain = email[1].split('@')
            providers = domain[1].split('.')[0]

            # Check if the provider length is greater than 5, which is our condition to consider a provider
            # suspicious.
            if len(providers) < 5:
                # Raises an BlackListProviderException otherwise
                raise BlackListProviderException('Email contains an invalid provider.')
