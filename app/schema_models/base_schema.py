from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class SchemaBase(BaseModel):
    is_active: bool = Field(title="User Status")
    created_by: Optional[str] = Field(title="Creator Name")
    created_on: Optional[datetime] = Field(title="Created Date")
    modified_by: Optional[str] = Field(title="Last Modifier Name")
    modified_on: Optional[datetime] = Field(title="Last Modified Time")
