import uuid
from datetime import datetime
from sqlalchemy import Boolean, TIMESTAMP, String, Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(UUID(as_uuid=True), primary_key=True, unique=True, index=True, default=uuid.uuid4)
    email = Column(String, unique=True, nullable=False)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)

    tasks = relationship("Task", back_populates="user")


class Task(Base):
    __tablename__ = "task"

    task_id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"))
    text = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    status = Column(Boolean, default=False)

    user = relationship("User", back_populates="tasks")


# # new_user = user(
# #                ^^^^^
# # TypeError: 'Table' object is not callable
#
#
# user = Table(
#     "user",
#     metadata,
#     Column("id", UUID(as_uuid=True), primary_key=True, unique=True, index=True, default=uuid.uuid4),
#     Column("email", String, unique=True, nullable=False),
#     Column("username", String, unique=True, nullable=False),
#     Column("password", String, nullable=False),
#     Column("registered_at", TIMESTAMP, default=datetime.utcnow),
#     Column("is_active", Boolean, default=True)
# )
#
# task = Table(
#     "task",
#     metadata,
#     Column("task_id", UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4),
#     Column("user_id", UUID(as_uuid=True), ForeignKey("user.id")),
#     Column("text", String, nullable=False),
#     Column("created_at", TIMESTAMP, default=datetime.utcnow),
#     Column("status", Boolean, default=False)
# )
