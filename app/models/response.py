from app.models.base_model import BaseModel, AuditCreateModel, AuditUpdateModel
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import ForeignKey, Column, Boolean
from app.models import User, Questions


class Response(BaseModel, AuditCreateModel, AuditUpdateModel):
    __tablename__ = "responses"

    user_id = Column(UUID(as_uuid=True), ForeignKey(User.id), nullable=False)
    question_id = Column(UUID(as_uuid=True), ForeignKey(Questions.id), nullable=False)
    response = Column(Boolean, nullable=False)
