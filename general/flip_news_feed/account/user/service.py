from general.flip_news_feed.account.service import AccountService
from general.flip_news_feed.account.user.dao import UserDao
from general.flip_news_feed.account.user.exceptions import InvalidFollowOperation, InvalidUserOperation, UserAuthFailedException
from general.flip_news_feed.account.user.model import User


class UserService(AccountService):
    def __init__(self):
        super(UserService, self).__init__()
        self.user_model = User
        self.user_dao = UserDao()

    def login_user(self, account_id, user_entered_password):
        account_authorized = self.is_account_authorized(account_id, user_entered_password)
        if not account_authorized:
            raise UserAuthFailedException()

    def create_new_user(self, **creation_kwargs):
        new_user = self.user_model()
        new_user.name = creation_kwargs.pop("name")
        new_user.user_name = creation_kwargs.pop("user_name", None)
        new_user.phone_number = creation_kwargs.pop("phone_number", None)
        new_user.email = creation_kwargs.pop("email", None)
        self.user_dao.add_user_by_account_id(new_user.account_id, new_user)
        return new_user.account_id

    def get_user_details(self, account_id):
        return self.user_dao.get_account_details_by_account_id(account_id)

    def follow_user(self, user_id_1, user_id_2):
        # exception handling
        user_1 = self.user_dao.get_account_details_by_account_id(user_id_1)
        if not user_1:
            raise InvalidFollowOperation("{0} user doesn't exist".format(str(user_id_1)))
        user_2 = self.user_dao.get_account_details_by_account_id(user_id_2)
        if not user_2:
            raise InvalidFollowOperation("{0} user doesn't exist".format(str(user_id_2)))
        user_1.following_users.add(user_id_2)

    def get_following_users(self, user_id):
        user = self.user_dao.get_account_details_by_account_id(user_id)
        if user:
            return user.following_users
        raise InvalidUserOperation("user doesn't exists")
