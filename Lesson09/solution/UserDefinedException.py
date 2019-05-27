class EmailNotValidError(BaseException):
    """ Raised when the target email is not valid """

    def __init__(self, m):
        self.message = m

    def __str__(self):
        return self.message
