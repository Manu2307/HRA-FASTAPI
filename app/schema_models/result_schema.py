from pydantic import BaseModel, UUID4, Field
from typing import List
from uuid import UUID
from app.schema_models.base_schema import SchemaBase


class CreateCombinationRequest(BaseModel):
    combination: List[UUID] = Field(title="Combinations")
    conclusion: str = Field(title="Conclusion")
    recommendation: str = Field(title='Recommendation')


class CreateCombinationResponse(SchemaBase):
    id: UUID4 = Field(title="Unique ID of the combination")
    combination: List[UUID] = Field(title="Combinations")
    conclusion: str = Field(title="Conclusion")
    recommendation: str = Field(title='Recommendation')

    class Config:
        from_attributes = True


class CreateBunchCombinationRequest(BaseModel):
    data: List[CreateCombinationRequest]


class CreateBunchCombinationResponse(BaseModel):
    response: List[CreateCombinationResponse]
