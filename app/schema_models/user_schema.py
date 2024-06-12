from pydantic import BaseModel, Field
from app.schema_models.base_schema import SchemaBase
from uuid import UUID


class RegisterUserRequest(BaseModel):
    email: str = Field(..., min_length=17, max_length=55, pattern='[a-zA-Z_.]@senecaglobal.com', title="Email",
                       examples=["manojkumar.andhrapu@senecaglobal.com", "sumaja.gurlinka@senecaglobal.com"])
    name: str = Field(..., title="Name")


class CreateUserResponse(SchemaBase):
    id: UUID = Field(..., title="User ID")
    email: str = Field(..., title="Email")
    name: str = Field(..., title="Name")

    class Config:
        from_attributes = True
