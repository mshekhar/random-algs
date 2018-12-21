from general.flip_news_feed.account.dao import AccountDao


class UserDao(AccountDao):
    def __init__(self):
        self.users = {}
        super(UserDao, self).__init__()

    def get_account_details_by_account_id(self, account_id):
        return self.users.get(account_id)

    def add_user_by_account_id(self, account_id, user_obj):
        self.users[account_id] = user_obj

    def update_user_by_account_id(self, account_id, update_spec):
        self.users[account_id].update(update_spec)
