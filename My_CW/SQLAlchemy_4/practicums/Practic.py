from decimal import Decimal

from pydantic import BaseModel,ConfigDict

from sqlalchemy import (create_engine,
                        Numeric,
                        BigInteger,
                        Column,
                        String,
                        SmallInteger,
                        Boolean,
                        Integer,
                        ForeignKey)
from sqlalchemy.orm import (sessionmaker,
                            DeclarativeBase,
                            Mapped,
                            mapped_column,
                            relationship)
from pathlib import Path


class Base(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        unique=True,
        autoincrement=True
    )

    """ТЕХНИЧЕСКОЕ ЗАДАНИЕ:
Создать модель минерала для системы управления поставками драгоценных камней.

ТРЕБОВАНИЯ:
- Уникальный идентификатор (BigInteger, автоинкремент)
- Название минерала (строка, максимум 50 символов, уникальное)
- Цвет минерала (строка, максимум 30 символов)
- Твердость по шкале Мооса (число с плавающей точкой)

ЦЕЛЬ: Создать основу для каталога минералов, которые будут поставляться в салоны."""


class Minerals(Base):
    __tablename__ = "minerals"


neme: Mapped[str] = mapped_column(
    String(50),
    unique=True,
nullable = False
)

color: Mapped[int] = mapped_column(
    String(30),
    nullable=False

)
hardness: Mapped[Decimal] = mapped_column(
    Numeric(4, 2),
    nullable=False

)

engine = create_engine("sqlite:///minerals.db")
Base.metadata.create_all(engine)


