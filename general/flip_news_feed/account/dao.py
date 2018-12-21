from abc import ABCMeta


class AccountDao(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    def get_account_details_by_account_id(self, account_id):
        raise NotImplementedError()
