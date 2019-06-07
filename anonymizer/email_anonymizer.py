"""Email anonymizer module."""

from base_anonymizer import BaseAnonymizer
import re

class EmailAnonymizer(BaseAnonymizer):
    """Email anonymizer.

    Sample usages (parametrized):
    >>> EmailAnonymizer('...').anonymize('aaa@aaa.com')
    '...@aaa.com'
    >>> EmailAnonymizer('***').anonymize('a-a@a.b.c')
    '***@a.b.c'
    >>> EmailAnonymizer('XXX').anonymize('a.d+a@a-a.com')
    'XXX@a-a.com'
    """

    def __init__(self, replacement):
        """
        :param str replacement:
        """
        self._replacement = replacement

    def anonymize(self, text):
        """
        :param str text:
        :rtype: str
        """
        search_part = re.search('.*(@.*)',text)
        output_string = self._replacement + search_part.group(1)
        return(output_string)
        #
        # @TODO: Implement it
        #
EmailAnonymizer('...').anonymize('aaa@aaa.com')
EmailAnonymizer('***').anonymize('a-a@a.b.c')
EmailAnonymizer('XXX').anonymize('a.d+a@a-a.com')
