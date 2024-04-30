import uuid
from datetime import datetime
from sqlalchemy import Boolean, TIMESTAMP, String, Integer, Table, Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from .database import metadata


user = Table(
    "user",
    metadata,
    Column("id", UUID(as_uuid=True), primary_key=True, unique=True, index=True, ),
    Column("email", String, unique=True, nullable=False),
    Column("username", String, unique=True, nullable=False),
    Column("password", String, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    Column("is_active", Boolean, default=True)
)

task = Table(
    "task",
    metadata,
    Column("task_id", UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4),
    Column("user_id", UUID(as_uuid=True), ForeignKey("user.id")),
    Column("text", String, nullable=False),
    Column("created_at", TIMESTAMP, default=datetime.utcnow),
    Column("status", Boolean, default=False)
)
