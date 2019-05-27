from operator import itemgetter


def update_mailing_list_extended(mailing_list):
    """
        This function updates the mailing list of a CRM (Customer Relationship Management) system. It receives the
        original mailing list and filter out users that have unsubscribed from the list. The unsubscribed flag includes
        `opt-out`, `OPT-OUT`, and `unsubscribed`. Also, the system now only permits professional email addresses.
        Therefore, emails with the `@gmail` provider must be excluded as well.

        The remaining users are considered to be active.

    :param mailing_list: the original mailing list with all the users
    :return ids: the list of ids of the active users


    Example:

        input original mailing list:

            1. 055dff79-7d09-4194-95f2-48dd586b8bd7': ['mknapton8', 'vlewndenh@spiegel.de', 'active']
            2. 5216dc65-05bb-4aba-a516-3c1317091471': ['ajelf9', 'kmacpaikei@purevolume.com', 'unsubscribed']
            3. d08649ee-62ae-4d1a-b578-fdde309bb721': ['tstodart5', 'schasmoor7@gmail.com', 'active']

        output updated mailing list:

            1. 055dff79-7d09-4194-95f2-48dd586b8bd7': ['mknapton8', 'vlewndenh@spiegel.de', 'active']

        User 2 has been filtered out because he has the flag `unsubscribed`, and, therefore, is not an active user
        anymore.

        User 3 has the `active` flag. However, the email provider is `@gmail`, which is not a professional
        email address. For this reason, we also remove it.

        The only `active` user we have to keep in the list is the user 1.

    """

    # Creating a copy of the original mailing list
    # This is necessary because we are going to exclude some keys (pop)
    mailing_list_copy = dict(mailing_list)

    # Looping over the mailing list and extracting key and value
    for key, value in mailing_list_copy.items():

        # Checks it the flag `opt-out` is present. We use lower() here to lowercase the flags and contemplate both
        # `opt-out` and `OPT-OUT` cases
        # Then, checks for the presence of the `unsubscribed` flag Finally,
        # checks if the email address contains `@gmail` provider
        if ('opt-out' in value[2].lower()) or \
                ('unsubscribed' in value[2].lower()) or \
                ('@gmail' in value[1]):
            # Remove the key if one of the above conditions is satisfied
            mailing_list.pop(key)

    # An array to collect the final output
    ids = []

    # Sort the updated mailing list alphabetically by `nickname`
    for items in sorted(mailing_list.items(), key=itemgetter(1), reverse=False):
        # Appending only the ids of the active users
        ids.append(items[0])

    # Returns the updated mailing list with the active users
    return ids
