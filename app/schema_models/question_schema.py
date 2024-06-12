from pydantic import BaseModel, Field
from app.schema_models.base_schema import SchemaBase
from uuid import UUID
from typing import Optional, List


class CreateQuestionRequest(BaseModel):
    question: str = Field(..., min_length=10, title="Question", examples=["How are you?"])
    type: str = Field(..., min_length=3, max_length=55, title="Question Type", examples=["Nutrition"])


class CreateQuestionResponse(SchemaBase):
    id: UUID = Field(..., title="User ID")
    question: str = Field(..., title="Question")
    type: str = Field(..., title="Question Type")

    class Config:
        from_attributes = True


class CreateQuestionsRequest(BaseModel):
    data: List[CreateQuestionRequest]


class CreateQuestionsResponse(BaseModel):
    response: List[CreateQuestionResponse]


class UpdateQuestionRequest(BaseModel):
    question: Optional[str] = Field(min_length=10, title="Question", examples=["How are you?"])
    type: Optional[str] = Field(min_length=3, max_length=55, title="Question Type", examples=["Nutrition"])
