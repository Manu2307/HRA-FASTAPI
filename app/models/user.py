from app.models.base_model import BaseModel, AuditCreateModel, AuditUpdateModel
from sqlalchemy import Column, String


class User(BaseModel, AuditCreateModel, AuditUpdateModel):
    __tablename__ = "user"
    # __table_args__ = (
    #     {"schema": "application"},
    # ) If you want to have schema, use this format

    name = Column(String(55), unique=True)
    email = Column(String(55), unique=True)
