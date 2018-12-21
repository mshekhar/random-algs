from general.flip_news_feed.account.model import Account


class User(Account):
    def __init__(self):
        self._name = None
        self._email = None
        self._phone_number = None
        self._user_name = None
        self.following_users = set()
        super(User, self).__init__()
        self.account_id = self.name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
        self.account_id = name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        self._phone_number = phone_number

    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        self._user_name = user_name
