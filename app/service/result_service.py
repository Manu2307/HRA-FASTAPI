from app.lib.singleton import Singleton
from fastapi.logger import logger
from app.repository import ResultOperations
from app.lib.custom_exceptions import CreateRecordException
from uuid import UUID


class ResultService(metaclass=Singleton):

    @staticmethod
    def create_combination(create_data):
        logger.info("Service called - create_combination")
        try:
            record = ResultOperations().create_combination(create_data)
        except Exception as ex:
            raise CreateRecordException("Unable to create record")

        return record

    @staticmethod
    def create_bunch_combinations(create_data):
        logger.info("Service called - create_bunch_combinations")
        try:
            record = ResultOperations().create_bunch_combinations(create_data)
        except Exception as ex:
            raise CreateRecordException("Unable to create record")

        return record

    @staticmethod
    def get_conclusion(user_id: UUID):
        logger.info("Service called - get_conclusion")
        try:
            record = ResultOperations().get_conclusion(user_id)
        except Exception as ex:
            print("Error in Repo layer")

        return record
