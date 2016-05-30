from decimal import Decimal

class Coercion(object):
    """
    Class used to make coertion between data returned from Base and data usable for developer
    """

    @staticmethod
    def to_decimal(value):
        """
        Coerce a value into a Decimal

        :param str value: a value to be coerced
        """
        return Decimal(value)