from app.lib.singleton import Singleton
from app.models import Response
from app.repository.sql_context import SqlContext


class ResponsesOperations(metaclass=Singleton):
    def __init__(self):
        self.model = Response

    @staticmethod
    def create_user_responses(user_data):
        user_response_data = []
        with SqlContext() as sql_context:
            for response in user_data.responses:
                user_response = Response()
                user_response.set_attributes(response)
                user_response.user_id = user_data.user_id
                sql_context.session.add(user_response)
                user_response_data.append(user_response)
        return user_response_data



