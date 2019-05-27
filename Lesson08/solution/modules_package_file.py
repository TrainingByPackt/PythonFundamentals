import csv

from Lesson08.solution.update_mailing_list import update_mailing_list

# Global variable to set the base path to our dataset folder
base_url = '../dataset/'


def read_mailing_list_file(filename, io_mode):
    """
        This function reads in the original dataset from a `csv` file, transforms it in a python dictionary, which
        is the same format we used on the functions exercise on chapter 4, and pass the data to the
        `update_mailing_list_extended` function to filter out the `unsubscribed` users. After that, we return the ids
        of the active users.

    :param filename: the filename of the original dataset we are going to read the data from.
    :param io_mode: the `input/output` mode we will use to handle the file operation.
    :return: the list of ids of the active users.

    """

    # Open the file with the `with` context manager
    with open(base_url + filename, io_mode) as csv_file:

        # Opening the csv file, passing the ',' delimiter, which is generally the case for csv files
        file_reader = csv.reader(csv_file, delimiter=',')

        # Declaring a counter to control the number of lines from dataset
        line_count = 0

        # Declaring a list variable to hold the rows read from file
        mailing_list = []

        # Looping through each row of the file
        for row in file_reader:

            # Check if the line is not 0 (that is, not the header)
            if line_count != 0:
                # Append each line to the `mailing_list` variable, excluding the header
                mailing_list.append(row)

            # Increment 1 to the counter
            line_count += 1

    # Create another list variable that will be used as a temporary buffer to transform our previous list into a
    # dictionary, which is the data structure expected from the `update_mailing_list_extended` function
    mailing_list_buffer = []

    # Looping through the mailing list object
    for item in mailing_list:
        # Creating tuples with each row in the original list
        mailing_list_buffer.append((item[0], [item[1], item[2], item[3]]))

    # Transforming the list of tuples into a python dictionary
    mailing_dict = (dict(mailing_list_buffer))

    # Call the `update_mailing_list_extended` from chapter 4 passing the mailing list dictionary
    updated_mailing_list_ids = update_mailing_list(mailing_dict)

    # Return the resulting ids of the active users
    return updated_mailing_list_ids


def save_output_file(updated_mailing_list, output_filename, io_mode):
    """
        This functions receives the list of ids of the active users (or updated mailing list) and saves the data
        into another file.

    :param updated_mailing_list: the list of ids of the active users in our CRM system database.
    :param output_filename: the name of the output file that will persist the users ids.
    :param io_mode: the `input/output` mode we will use to handle the file operation.
    :return: N/A
    """

    # Open the output file with the `with` context manager
    with open(base_url + output_filename, io_mode) as active_users_file:
        # Create a csv_writer object that will be responsible to persist the active users ids to a resulting
        # csv file. Note: In order to make the final output clearer and similar to the chapter 4 function output,
        # we are using the '\n' delimiter to write the results to file. That means that the output file will not be
        # comma separated (as csv implies), but it is still a csv file.
        csv_writer = csv.writer(active_users_file, delimiter='\n', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # Writing each user id as a new row to the file
        csv_writer.writerow(updated_mailing_list)


def mailinglist_validation_util(filename, output_filename, io_mode):
    """
        This function is the main entry point to trigger the other functions to handle file operations. First, we call
        the `read_mailing_list_file` to read the original dataset and process it with the `update_mailing_list_extended`
        function from chapter 4. Then, we cache the resulting active users ids list.

        Next, we call the `save_output_file` function to persist the users ids to an output csv file.

        Finally, we compute the length of the output file to check if it matches the result of our previous function
        to update the mailing list.

        To call this function, we need to provide some parameters: `filename`, `output_filename` and the `io_mode`.

        In order to play with the different i/o operations in python, we are going to send the io_mode parameter as a
        list ['r+', 'w+'] with the reading/writing operations separately. We could have done this with a single
        file operation, though.

        Example:

            mailinglist_validation_util('mailing_list.csv', 'output.csv', ['r+', 'w+'])

    :param filename: the name of the original dataset. In our case it's `mailing_list.csv`.
    :param output_filename: the name of the output file with the persisted ids for the active users. In our case
    it's `output.csv`.
    :param io_mode: array with the file operations for each function (`read_mailing_list_file` and `save_output_file`).
    :return: the length of the output file. We return this length to check it matches our previous update mailing ist
    function from chapter 4.

    """

    # Call the function to read the original mailing list file and cache the results from the function
    updated_mailing_list = read_mailing_list_file(filename, io_mode[0])

    # Call the function to write the results back to a csv file
    save_output_file(updated_mailing_list, output_filename, io_mode[1])

    # The sum of lines for the output file could have been done this way as well. Considering we are passing a list
    # of the active users ids to persist, and there is no processing in between, we could call `len()` directly on the
    # list we are passing to the `save_output_file` function.
    # output_file_length = (len(updated_mailing_list))

    # Open output file to count the number of lines written
    output_file = open(base_url + output_filename)

    # Sum 1 for each line of the output file
    output_file_length = (sum(1 for _ in output_file))

    # Closing the output file
    output_file.close()

    # Return the output file length
    return output_file_length
