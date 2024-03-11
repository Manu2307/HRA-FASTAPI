from app.repository import UserOperations
from app.lib.custom_exceptions import DuplicateRecordError, DBFetchFailureException, CreateRecordException


class UserService:

    @staticmethod
    def register_user(register_data):
        existing_user = UserService.get_user_by_email_id(register_data.email)

        if existing_user:
            raise DuplicateRecordError("User already exists")
        try:
            user_details = UserOperations.register_user(register_data)
        except Exception as ex:
            raise CreateRecordException("An error has occured while registering the new user")

        return user_details

    @staticmethod
    def get_user_by_id(user_id):
        try:
            user_details = UserOperations().get_user_by_id(user_id)
        except Exception as ex:
            print("HIIIIIII", str(ex))
            raise DBFetchFailureException("Unable to fetch the User")

        return user_details

    @staticmethod
    def get_user_by_email_id(email_id):
        try:
            user_details = UserOperations().get_user_by_email_id(email_id)
        except Exception as ex:
            raise DBFetchFailureException("Unable to fetch the User.")

        return user_details




