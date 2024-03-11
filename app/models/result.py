from app.models import BaseModel, AuditCreateModel, AuditUpdateModel
from sqlalchemy import Column, ARRAY, String
from sqlalchemy.dialects.postgresql import UUID


class Result(BaseModel, AuditCreateModel, AuditUpdateModel):
    __tablename__ = "result"

    combination = Column(ARRAY(UUID), nullable=False)
    conclusion = Column(String, nullable=False)
    recommendation = Column(String, nullable=False)
