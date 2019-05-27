from solution import modules_package_file as mlu


def mailing_list_utils_extended():
    """
        This function checks if the mailing list validation function is working from a package. We import it
        from a package and called it 'mlu'. This function must output the same result from the previous challenge.

    :return: the output of the `mailinglist_validation_util` function
    """

    # Returning the output of the `mailinglist_validation_util`, which must be the length of the output file with the
    # list of active users ids
    return mlu.mailinglist_validation_util('mailing_list.csv', 'output.csv', ['r+', 'w+'])


if __name__ == '__main__':
    # Calling the function from a package
    print('The output file has length {}.'.format(mailing_list_utils_extended()))
