from app.lib.singleton import Singleton
from fastapi.logger import logger
from app.repository import ResponsesOperations
from app.lib.custom_exceptions import CreateRecordException


class ResponseService(metaclass=Singleton):

    @staticmethod
    def create_user_responses(user_data):
        logger.info("Service called - create_user_responses")
        try:
            user_responses = ResponsesOperations().create_user_responses(user_data)
        except Exception as ex:
            raise CreateRecordException("Unable to submit the data")
        return user_responses
