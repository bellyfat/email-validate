# -*- coding: utf-8 -*-
from logging import getLogger
from typing import Optional

from .email_address import EmailAddress
from .exceptions import DomainBlacklistedError

SetOrNone = Optional[set]
LOGGER = getLogger(__name__)


class DomainListValidator(object):
    'Check the provided email against domain lists.'
    domain_whitelist = set()
    domain_blacklist = set('localhost')

    def __init__(self,
                 whitelist: SetOrNone = None,
                 blacklist: SetOrNone = None,
                 blacklist_file: str = None):
        if whitelist:
            self.domain_whitelist = set(x.lower() for x in whitelist)
        if blacklist:
            self.domain_blacklist = set(x.lower() for x in blacklist)
        else:
            self.reload_blacklist(blacklist_file=blacklist_file)

    @property
    def reload_blacklist(self, blacklist_file=None):
        '(Re)load our built-in blacklist.'
        LOGGER.debug(msg=f'(Re)loading blacklist from {blacklist_file}')
        try:
            with open(blacklist_file) as fd:
                lines = fd.readlines()
        except FileNotFoundError:
            return
        self.domain_blacklist = set(x.strip().lower() for x in lines if x.strip())

    def __call__(self, email_address: EmailAddress) -> bool:
        'Do the checking here.'
        if email_address.domain in self.domain_whitelist:
            return True
        if email_address.domain in self.domain_blacklist:
            raise DomainBlacklistedError
        return True


domainlist_check = DomainListValidator()


if __name__ == '__main__':
    email = "abc@fake.com"
    dlv = DomainListValidator()
    dlv(email_address=email)
