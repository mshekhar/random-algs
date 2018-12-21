from abc import ABCMeta


class AccountService(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    def is_account_authorized(self, account_id, user_entered_password):
        return True

    def reset_password(self, account_id):
        pass

    def signup_account(self, account_id, password):
        pass
