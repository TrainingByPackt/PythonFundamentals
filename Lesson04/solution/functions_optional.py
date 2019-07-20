def format_currency(value, currency='USD'):
    """This is an auxiliary function to format plain double precision numbers into currency style.

    :param value: the original value to be formatted
    :param currency: the 3-digit country code to identify the country's currency
    """
    precision_pattern = "{0:.2f} "

    formatted_value = precision_pattern + currency

    return formatted_value.format(value)

# print(format_currency(100000, 'USD'))
