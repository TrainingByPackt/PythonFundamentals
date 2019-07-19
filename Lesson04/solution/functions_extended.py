from Lesson04.solution.functions import calculate_gains

from Lesson04.solution.functions_optional import format_currency


# not official way to calculate "gains" over money investment
def calculate_gains_over_time(amount_inv=0.0, period=6):
    """
    Calculating the return gains of a given amount invested based on a period of application.

    :param amount_inv: the money amount invested
    :param period: application period
    :return:
    """

    # call the base `calculate_gains` function to estimate the gains for the first period
    total_amount_gains, total_gains, gain_margin = calculate_gains(amount_inv)

    # control variable to store the accumulated gains over the invested amount
    acc_gains = 0

    # calculate the first period before entering the loop
    new_amount = total_amount_gains

    # loop through the specified period to calculate the gain of each month
    # 1 to period -1 because the first period gains is already calculated above
    for i in range(1, period):
        print('month:{} - new_amount: {} '.format(i + 1, format_currency(new_amount, 'USD')))

        # call the function to update the value based on the period inside the loop and the updated amount
        total_amount_gains, total_gains, gain_margin = calculate_gains(new_amount)

        new_amount = total_amount_gains  # update the `new_amount` variable

        # print(total_gains)
        acc_gains += total_gains

    # return
    return amount_inv + acc_gains, acc_gains


#print(calculate_gains_over_time(amount_inv=10000, period=12))
