from app.lib.singleton import Singleton
from app.models import Result
from app.repository import CommonDbOperations
from app.repository.sql_context import SqlContext
from app.models import Response
from sqlalchemy import and_


class ResultOperations(metaclass=Singleton):
    def __init__(self):
        self.model = Result

    def create_combination(self, create_data):
        result = CommonDbOperations(self.model).create_record(create_data)

        return result

    def create_bunch_combinations(self, create_data):
        result = CommonDbOperations(self.model).create_bunch_of_records(create_data)

        return result

    @staticmethod
    def get_conclusion(user_id):
        with SqlContext() as sql_context:
            response_ids = []
            conclusions = {}
            records = sql_context.session.query(Response).filter(
                and_(Response.user_id == user_id, Response.response == False)).all()
            for record in records:
                response_ids.append(str(record.question_id))
            combinations = sql_context.session.query(Result).all()
            for record in combinations:
                for question in record.combination:
                    status = True
                    if question not in response_ids:
                        status = False
                        break
                if status:
                    conclusions[len(conclusions)+1] = {'conclusion': record.conclusion, 'recommendation': record.recommendation}
        return conclusions
