import prembly




class PremblyException(Exception):
    """The base exception class for all PremblyException"""
    pass


class MissingAuthKeyError(PremblyException):
    """
    We can't find the authentication/authorization key
    """
    pass


class InvalidMethodError(PremblyException):
    """
    Http method error class
    """
    pass

class MissingRequiredDataError(PremblyException):
    """
    Missing data error class
    """
    pass