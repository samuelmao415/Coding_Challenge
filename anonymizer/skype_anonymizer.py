"""Skype username anonymizer module."""

from base_anonymizer import BaseAnonymizer
import re

class SkypeUsernameAnonymizer(BaseAnonymizer):
    """Skype username anonymizer.

    Sample usages (parametrized):
    >>> SkypeUsernameAnonymizer('#').anonymize('<a href="skype:loren?call"/>')
    '<a href="skype:#?call"/>'
    >>> SkypeUsernameAnonymizer('#').anonymize('<a href="skype:LOREN?chat"/>')
    '<a href="skype:#?chat"/>'
    """

    def __init__(self, replacement):
        """
        :param str replacement:
        """
        self._repl = replacement

    def anonymize(self, text):
        """
        :param str text:
        :rtype: str
        """
        anonymized_text_p1 = re.sub('(<a href="skype:).*\?.*"/>','\\1',text)
        anonymized_text_p2 = re.sub('<a href="skype:.*(\?.*)','\\1',text)
        anonymized_text = anonymized_text_p1 + self._repl + anonymized_text_p2
        return anonymized_text
        #
        # @TODO: Implement it
        #
SkypeUsernameAnonymizer('#').anonymize('<a href="skype:loren?call"/>')
SkypeUsernameAnonymizer('#').anonymize('<a href="skype:LOREN?chat"/>')
