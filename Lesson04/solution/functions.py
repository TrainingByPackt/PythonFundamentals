# global variable
multiplier_amount = 1e6  # 1 million


def calculate_gains(amount_inv=0.0):
    """ Calculating the return gains from an investment.

    Example:

    amount_inv = 1000

    `calculate_gains(amount_inv)`


    :param amount_inv: the monetary amount to be invested

    :return total_amount_gains:
    """

    # base amount gain margin
    gain_margin = .001

    # check whether the invested amount is greater than the multiplier amount
    if amount_inv > multiplier_amount:
        # gather the mod of the division
        mod = amount_inv // multiplier_amount

        # update the `gain_margin` by the multiplier mod
        gain_margin = 1 * gain_margin * mod

    # calculate the total amount with gains
    total_amount_gains = (amount_inv * gain_margin) + amount_inv

    # calculate the total amount plus the gain margin
    total_gains = amount_inv * gain_margin

    # return
    return total_amount_gains, total_gains, gain_margin


# print(calculate_gains(amount_inv=2000000))


# not official way to calculate "gains" over money investment
def calculate_gains_over_time(amount_inv=0.0, period=6):
    """
    Calculating the return gains from an investment.

    :param amount_inv:
    :param period:
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
        print('month:{} - new_amount: {} '.format(i + 1, new_amount))

        # call the function to update the value based on the period inside the loop and the updated amount
        total_amount_gains, total_gains, gain_margin = calculate_gains(new_amount)

        new_amount = total_amount_gains  # update the `new_amount` variable

        # print(total_gains)
        acc_gains += total_gains

    # return
    return amount_inv + acc_gains, acc_gains


print(calculate_gains_over_time(amount_inv=100, period=12))

# let as todo => format currency (usd), precision (2)
