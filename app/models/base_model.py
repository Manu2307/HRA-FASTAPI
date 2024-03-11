from pydantic import UUID4
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from datetime import datetime
import json

from config import DB_DRIVER, DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME, SQLALCHEMY_DATABASE_URL

# SQLALCHEMY_DATABASE_URL = f"{DB_DRIVER}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, pool_pre_ping=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    def set_attributes(self, values):
        if not isinstance(values, dict):
            values = json.loads(values.json())

        for key, value in values.items():
            if (hasattr(self, key) and
                    ((isinstance(value, str) and value) or (isinstance(value, (bool, int, float, list, UUID4))))):
                setattr(self, key, value)


class AuditCreateModel(Base):
    __abstract__ = True
    created_at = Column(DateTime, default=datetime.now())
    created_by = Column(String, default="System")


class AuditUpdateModel(Base):
    __abstract__ = True
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now())
    updated_by = Column(String, default="System")
