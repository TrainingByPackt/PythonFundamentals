class BlackListProviderException(BaseException):
    """ Raised when the email provider is not valid, or less than 5-characters long. """

    def __init__(self, m):
        self.message = m

    def __str__(self):
        return self.message
