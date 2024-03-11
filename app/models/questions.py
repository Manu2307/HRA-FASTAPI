from app.models.base_model import BaseModel, AuditCreateModel, AuditUpdateModel
from sqlalchemy import Column, String


class Questions(BaseModel, AuditCreateModel, AuditUpdateModel):
    __tablename__ = "questions"

    question = Column(String, nullable=False)
    type = Column(String(55), nullable=False)
