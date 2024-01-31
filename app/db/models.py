from datetime import datetime
from sqlalchemy import Boolean, TIMESTAMP, String, Integer, Table, Column, MetaData, ForeignKey


metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, index=True, autoincrement=True),
    Column("email", String, unique=True, nullable=False),
    Column("username", String, unique=True, nullable=False),
    Column("password", String, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    Column("is_superuser", Boolean, default=False)
)

tasks = Table(
    "tasks",
    metadata,
    Column("id", Integer, primary_key=True, index=True, autoincrement=True),
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("text", String, nullable=False),
    Column("timestamp", TIMESTAMP, default=datetime.utcnow),
    Column("status", Boolean, default=False)
)


