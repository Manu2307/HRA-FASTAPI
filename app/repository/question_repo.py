from app.lib.singleton import Singleton
from app.models import Questions
from app.repository.common_ops import CommonDbOperations
from app.repository.sql_context import SqlContext
from app.schema_models import UpdateQuestionRequest


class QuestionOperations(metaclass=Singleton):
    def __init__(self):
        self.model = Questions

    def create_question(self, question_data):

        question_details = CommonDbOperations(self.model).create_record(question_data)

        return question_details

    def create_bunch_of_questions(self, questions_data):
        questions_details = CommonDbOperations(self.model).create_bunch_of_records(questions_data)

        return questions_details

    def get_question_by_id(self, question_id):
        question = CommonDbOperations(self.model).get_by_id(question_id)

        return question

    def get_questions_by_type(self, question_type):
        with SqlContext() as sql_context:
            question_details = sql_context.session.query(self.model).filter_by(type=question_type).all()

        return question_details

    @staticmethod
    def update_question(record: Questions, update_data: UpdateQuestionRequest):
        updated_record = CommonDbOperations.update_record(record, update_data)

        return updated_record

