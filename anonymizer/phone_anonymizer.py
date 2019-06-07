"""Phone number anonymizer module."""

from base_anonymizer import BaseAnonymizer
import re

class PhoneNumberAnonymizer(BaseAnonymizer):
    """Phone number anonymizer.

    Sample usages (parametrized):
    >>> PhoneNumberAnonymizer('X').anonymize('+48 666 777 888')
    '+48 666 777 XXX'
    >>> PhoneNumberAnonymizer('X', 5).anonymize('+48 666 777 888')
    '+48 666 7XX XXX'
    >>> PhoneNumberAnonymizer('*', 1).anonymize('+48 666 777 888')
    '+48 666 777 88*'
    >>> PhoneNumberAnonymizer('x', 9).anonymize('+55 666 777 000')
    '+55 xxx xxx xxx'
    """

    def __init__(self, replacement, last_digits=3):
        """
        :param str replacement:
        :param int last_digits:
        """
        self._repl = replacement
        self._digits = last_digits

    def anonymize(self, text):
        """
        :param str text:
        :rtype: str
        """
        text = text.replace(" ","")
        text
        replace_pos = self._digits
        text_result = text[:-replace_pos:] + self._repl * self._digits
        text_result = [text_result[i:i+3] for i in range(0, len(text_result), 3)]
        output_number = ' '.join(text_result)
        return(output_number)
        #
        # @TODO: Implement it
        #
PhoneNumberAnonymizer('*', 1).anonymize('+48 666 777 888')
PhoneNumberAnonymizer('x', 9).anonymize('+55 666 777 000')
PhoneNumberAnonymizer('X', 5).anonymize('+48 666 777 888')
