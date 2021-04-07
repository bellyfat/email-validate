from unittest.case import TestCase

from email_validate.domainlist_check import (
    domainlist_check, reload_blacklist)
from email_validate.email_address import EmailAddress
from email_validate.exceptions import DomainBlacklistedError
from email_validate.email_validate import (validate, validate_or_fail)


class BlacklistCheckTestCase(TestCase):
    'Testing if the included blacklist filtering works.'

    def setUpClass():
        reload_blacklist(force=False, background=False)

    def test_blacklist_positive(self):
        'Disallows blacklist item: mailinator.com.'
        with self.assertRaises(DomainBlacklistedError):
            domainlist_check(EmailAddress('pm2@mailinator.com'))
        with self.assertRaises(DomainBlacklistedError):
            validate_or_fail(
                email_address='pm2@mailinator.com', check_format=False,
                check_blacklist=True)
        with self.assertRaises(DomainBlacklistedError):
            validate_or_fail(
                email_address='pm2@mailinator.com', check_format=True,
                check_blacklist=True)
        with self.assertLogs():
            self.assertFalse(expr=validate(
                email_address='pm2@mailinator.com', check_format=False,
                check_blacklist=True))
        with self.assertLogs():
            self.assertFalse(expr=validate(
                email_address='pm2@mailinator.com', check_format=True,
                check_blacklist=True))

    def test_blacklist_negative(self):
        'Allows a domain not in the blacklist.'
        self.assertTrue(expr=domainlist_check(
            EmailAddress('pm2@some-random-domain-thats-not-blacklisted.com')))
