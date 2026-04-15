from sqlalchemy import create_engine, BigInteger, String, Boolean, Numeric, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from pathlib import Path
from typing import List, Optional


# OopCompanion:suppressRename


BASE_DIR = Path(__file__).parents[2]


engine = create_engine(
    url=f"sqlite:///:memory:"
)

class Base(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True,
        unique=True
    )

class Category(Base):
    __tablename__ = 'categories'


    name: Mapped[str] = mapped_column(
        String(100), nullable=False
    )

    description: Mapped[Optional[str]] = mapped_column(
        String(255), nullable=True
    )


    questions: Mapped[List["Question"]] = relationship(
        back_populates="category"
    )


    products: Mapped[List["Product"]] = relationship(
        "Product", back_populates="category"
    )

class Product(Base):
    __tablename__ = 'products'

    name: Mapped[str] = mapped_column(
        String(100), nullable=False
    )

    price: Mapped[Optional[float]] = mapped_column(
        Numeric(), nullable=True
    )

    is_stock: Mapped[bool] = mapped_column(
        Boolean, default=True
    )

    category_id: Mapped[Optional[int]] = mapped_column(
        BigInteger,
        ForeignKey("categories.id"),
        nullable=True
    )

    category: Mapped["Category"] = relationship(
        "Category", back_populates="products"
    )


class Question(Base):
    __tablename__ = "questions"

    text: Mapped[str] = mapped_column(
        String(500), nullable=False
    )

    answer: Mapped[str] = mapped_column(
        String(1000), nullable=False
    )

    category_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("categories.id"),
        nullable=False
    )

    category: Mapped["Category"] = relationship(
        "Category", back_populates="questions"
    )