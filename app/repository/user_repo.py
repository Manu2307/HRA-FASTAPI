from app.models import User
from app.repository.sql_context import SqlContext


class UserOperations:
    def __init__(self):
        self.model = User

    def register_user(self, user_details):
        user = self.model()
        user.set_attributes(user_details)

        with SqlContext() as sql_context:
            sql_context.session.add(user)

        return user

    def get_user_by_id(self, user_id):
        user = self.model()
        with SqlContext() as sql_context:
            user_details = sql_context.session.query(user).filter(user.id == user_id).scalar()

        return user_details

    def get_user_by_email_id(self, email_id):
        user = self.model()
        print("HI")
        with SqlContext() as sql_context:
            print("Hello")
            try:
                user_details = sql_context.session.query(user).filter(user.email == email_id).all()

            except Exception as ex:
                print(str(ex))

        return user_details
