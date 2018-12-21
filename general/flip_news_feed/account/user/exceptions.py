class InvalidUserOperation(Exception):
    pass


class InvalidFollowOperation(InvalidUserOperation):
    pass


class UserAuthFailedException(InvalidUserOperation):
    pass
