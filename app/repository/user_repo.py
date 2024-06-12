from app.models import User
from app.repository.sql_context import SqlContext
from app.lib.singleton import Singleton

from app.repository.common_ops import CommonDbOperations


class UserOperations(metaclass=Singleton):
    def __init__(self):
        self.model = User

    def register_user(self, user_details):
        user_details = CommonDbOperations(self.model).create_record(user_details)

        return user_details

    def get_user_by_id(self, user_id):
        user_details = CommonDbOperations(self.model).get_by_id(user_id)

        return user_details

    def get_user_by_email_id(self, email_id):
        user_details = CommonDbOperations(self.model).get_by_email(email_id)

        return user_details
