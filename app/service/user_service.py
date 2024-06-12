from app.repository import UserOperations
from app.lib.custom_exceptions import DuplicateRecordError, DBFetchFailureException, CreateRecordException
from app.lib.singleton import Singleton
from fastapi.logger import logger


class UserService(metaclass=Singleton):

    @staticmethod
    def register_user(register_data):
        logger.info("Service called - UserService.register_user")
        existing_user = UserService.get_user_by_email_id(register_data.email)
        if existing_user:
            logger.error(f"User already exists with the email_id - {register_data.email}")
            raise DuplicateRecordError(f"User already exists with the emailid - {register_data.email}")

        try:
            user_details = UserOperations().register_user(register_data)

        except Exception as ex:
            logger.error("An error has Occured")
            raise CreateRecordException("An error has occured while registering the new user")

        return user_details

    @staticmethod
    def get_user_by_id(user_id):
        logger.info("Service called - UserService.get_user_by_id")
        # user_details = CommonService.get_record_by_id(CommonDbOperations(User), user_id)
        try:
            user_details = UserOperations().get_user_by_id(user_id)
        except Exception as ex:
            raise DBFetchFailureException("Unable to fetch the User")

        return user_details

    @staticmethod
    def get_user_by_email_id(email_id):
        try:
            user_details = UserOperations().get_user_by_email_id(email_id)
        except Exception as ex:
            raise DBFetchFailureException("Unable to fetch the User.")

        return user_details




