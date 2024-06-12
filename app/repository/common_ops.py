from sqlalchemy import select
from app.repository.sql_context import SqlContext


class CommonDbOperations:
    def __init__(self, model):
        self.model = model
        # self.query = select(model)

    def create_record(self, create_data):
        record = self.model()
        record.set_attributes(create_data)
        with SqlContext() as sql_context:
            sql_context.session.add(record)

        return record

    def create_bunch_of_records(self, create_data):
        return_data = []
        with SqlContext() as sql_context:
            for each_item in create_data:
                record = self.model()
                record.set_attributes(each_item)
                sql_context.session.add(record)
                return_data.append(record)

        return return_data

    def get_all(self):
        with SqlContext() as sql_context:
            result = sql_context.session.query(self.model)

        return result.all()

    def get_by_id(self, record_id, commit=True):
        with SqlContext() as sql_context:
            result = sql_context.session.query(self.model).filter_by(id=str(record_id))

        return result.scalar()

    def get_by_email(self, email_id):
        with SqlContext() as sql_context:
            result = sql_context.session.query(self.model).filter_by(email=str(email_id))

        return result.scalar()

    @staticmethod
    def update_record(record, update_data):
        try:
            record.set_attributes(update_data)
            with SqlContext() as sql_context:
                sql_context.session.add(record)
        except Exception as ex:
            import traceback
            traceback.print_exc()
            print(str(ex))

        return record


