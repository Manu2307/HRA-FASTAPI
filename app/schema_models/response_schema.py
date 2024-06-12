from pydantic import Field, UUID4, BaseModel
from typing import List
from app.schema_models.base_schema import SchemaBase


class CreateResponseRequestData(BaseModel):
    question_id: UUID4 = Field("Question ID")
    response: bool = Field("User Response")


class CreateResponseRequest(BaseModel):
    user_id: UUID4 = Field(title="User ID")
    responses: List[CreateResponseRequestData]


class CreateResponseItem(SchemaBase):
    id: UUID4 = Field(..., title="Response ID")
    user_id: UUID4 = Field(title="User ID")
    question_id: UUID4 = Field("Question ID")
    response: bool = Field("User Response")

    class Config:
        from_attributes = True


class CreateResponseResponse(BaseModel):
    response: List[CreateResponseItem]
