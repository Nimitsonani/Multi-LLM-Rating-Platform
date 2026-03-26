import os
from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker
from sqlalchemy.orm import Mapped,mapped_column,DeclarativeBase,relationship
from sqlalchemy import ForeignKey,DateTime,func
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from dotenv import load_dotenv
import uuid

load_dotenv(dotenv_path='.env')
DB_URL = os.getenv('DATABASE_URL')
if DB_URL.startswith("postgres://"):
    DB_URL = DB_URL.replace("postgres://", "postgresql+asyncpg://", 1)


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users_table'
    id:Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    username:Mapped[str] = mapped_column(unique=True,nullable=False)
    email: Mapped[str] = mapped_column(unique=True,nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    all_rating: Mapped[list['Rating']] = relationship(lazy="selectin")

class Rating(Base):
    __tablename__ = 'ratings_table'
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    rating: Mapped[float] = mapped_column(nullable=False)
    model: Mapped[str] = mapped_column(nullable=False)
    created_at :Mapped[datetime] = mapped_column(DateTime(timezone=True),server_default=func.now())
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('users_table.id'))


engine = create_async_engine(DB_URL)

AsyncSessionLocal = async_sessionmaker(engine,expire_on_commit=False)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
