# global variable
multiplier_amount = 1e6  # 1 million


def calculate_gains(amount_inv=0.0):
    """ Calculating the return gains of an investment.

    Example:

    amount_inv = 1000

    `calculate_gains(amount_inv)`


    :param amount_inv: the monetary amount to be invested

    :return total_amount_gains: the total returns of the investment
    """

    # base amount gain margin
    gain_margin = .001

    total_amount_gains = 0

    total_gains = 0

    if amount_inv > 1000:

        # check whether the invested amount is greater than the multiplier amount
        if amount_inv > multiplier_amount:
            # gather the mod of the division
            mod = amount_inv // multiplier_amount

            # update the `gain_margin` by the multiplier mod
            gain_margin = ((1 + (mod / 100)) * gain_margin)

        # calculate the total amount with gains
        total_amount_gains = (amount_inv * gain_margin) + amount_inv

        # calculate the total amount plus the gain margin
        total_gains = amount_inv * gain_margin

    # return the invested amount plus the gains, the gains only and the gain margin
    return total_amount_gains, total_gains, gain_margin

# print(calculate_gains(amount_inv=2000000))
