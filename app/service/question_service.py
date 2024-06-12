from app.lib.singleton import Singleton
from uuid import UUID
from typing import List
from fastapi.logger import logger
from app.schema_models import CreateQuestionRequest, CreateQuestionResponse, UpdateQuestionRequest
from app.repository import QuestionOperations
from app.lib.custom_exceptions import (CreateRecordException, DBFetchFailureException, RecordNotFoundError,
                                       UpdateRecordError)


class QuestionService(metaclass=Singleton):

    @staticmethod
    def create_question(question_data: CreateQuestionRequest) -> CreateQuestionResponse:
        try:
            question_details = QuestionOperations().create_question(question_data)

        except Exception as ex:
            raise CreateRecordException("An error has occured while registering the new question")

        return question_details

    @staticmethod
    def create_bunch_of_questions(questions_data):
        logger.info("Service called - create_bunch_of_questions")
        try:
            questions_details = QuestionOperations().create_bunch_of_questions(questions_data)

        except Exception as ex:
            raise CreateRecordException("An error has occured while registering the new question")

        return questions_details

    @staticmethod
    def get_question_by_id(question_id: UUID) -> CreateQuestionResponse:
        try:
            question = QuestionOperations().get_question_by_id(question_id)
        except Exception as ex:
            raise DBFetchFailureException("Unable to fetch the record")

        if not question:
            raise RecordNotFoundError(f"No record exists with the id - {question_id}")

        return question

    @staticmethod
    def get_questions_by_type(question_type: str) -> List:
        try:
            questions = QuestionOperations().get_questions_by_type(question_type)
        except Exception as ex:
            raise DBFetchFailureException(f"Unable to fetch the questions of type - {question_type}")

        return questions

    @staticmethod
    def update_question(update_data: UpdateQuestionRequest, question_id: UUID):
        record = QuestionOperations().get_question_by_id(question_id)
        if not record:
            raise RecordNotFoundError(f"No record exists with the id - {question_id}")

        try:
            updated_question = QuestionOperations().update_question(record, update_data)
        except Exception as ex:
            raise UpdateRecordError(" Unable to process your request at the moment.")

        return updated_question
