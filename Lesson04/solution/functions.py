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

    gain_margin = .001

    if amount_inv > multiplier_amount:
        mod = amount_inv // multiplier_amount
        gain_margin = 1 * gain_margin * mod

    total_amount_gains = (amount_inv * gain_margin) + amount_inv
    total_gains = amount_inv * gain_margin

    return total_amount_gains, total_gains, gain_margin


print(calculate_gains(amount_inv=1000))


def calculate_gains_over_time(amount_inv=0.0, period=6):
    """ Calculating the return gains from an investment. """

    total_amount_gains, total_gains, gain_margin = calculate_gains(amount_inv)

    gains = 0

    for i in range(1, period):
        new_amount = total_amount_gains
        total_amount_gains, total_gains, gain_margin = calculate_gains(new_amount)
        print(total_gains)
        gains += total_gains

    return amount_inv + gains, gains


print(calculate_gains_over_time(amount_inv=100000, period=12))
