# Importing re library

# Importing user-defined exceptions


def is_provider_valid_blacklist_optional_len(mailing_list):
    """
        Your docstring documentation starts here.

        For more information on how to proper document your function, please refer to the official PEP8:
        https://www.python.org/dev/peps/pep-0008/#documentation-strings.
    """

    # Array to hold user ids
    final_users_list = []

    # The regex pattern to validate emails
    regex =  # The regex pattern to validate emails

    # Loop through the mailing list
    for key, email in  # Your mailing list:

        if '@' in ...  # Check if the @ is present in the email and check if the email passes the regex pattern
            # Append the id of users with valid emails

            # Extract only the provider from the email string

            # Inserted a try.., except.. block to cast the exception
            try:
                # Check if the provider length is greater than 5, which is our condition to consider a provider
                # suspicious.
                if  # Check if the provider contains at least 5 characters:
            # Append the id of users with email addresses with valid providers

            except  # Your user-defined exception:
        # Return a user-friendly message to cast the exception

    return final_users_list


def is_provider_valid_blacklist_optional_exception(mailing_list):
    """
        Your docstring documentation starts here.

        For more information on how to proper document your function, please refer to the official PEP8:
        https://www.python.org/dev/peps/pep-0008/#documentation-strings.
    """

    # The regex pattern to validate emails
    regex =  # The regex pattern to validate emails

    # Loop through the mailing list
    for key, email in  # Your mailing list:

        # Check if the @ is present in the email and check if the email passes the regex patter
        if '# Check if the email contains @ and passes the regex':
            # Append the id of users with valid emails

            # Extract only the provider from the email string

            # Check if the provider length is greater than 5, which is our condition to consider a provider
            # suspicious.
            if  # Check if the provider contains at least 5 characters:
        # raise your custom defined exception
