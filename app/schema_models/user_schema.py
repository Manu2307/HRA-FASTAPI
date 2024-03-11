from pydantic import BaseModel, Field, UUID4
from app.schema_models.base_schema import SchemaBase


class CreateUserRequest(BaseModel):
    email: str = Field(..., min_length=17, max_length=55, pattern='[a-zA-Z_.]@senecaglobal.com', title="Email",
                       examples=["manojkumar.andhrapu@senecaglobal.com", "sumaja.gurlinka@senecaglobal.com"])
    name: str = Field(..., title="Name")


class CreateUserResponse(SchemaBase):
    id: UUID4 = Field(title="User ID")
    email: str = Field(title="Email")
    name: str = Field(title="Name")
