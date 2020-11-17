class DomainException(Exception):
    """ Base class for domain exceptions """

class InvalidDorsalNumber(DomainException):
    """ Raised when a number is not valid in a dorsal """
