from sqlalchemy import create_engine, BigInteger, SmallInteger, String, Boolean
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column
from pathlib import Path


BASE_DIR = Path(__file__).parents[2]
print(__file__)
print(BASE_DIR)

engine = create_engine(
    url=f"sqlite:///{BASE_DIR / 'database.db'}"
)

Session = sessionmaker(
    bind=engine
)


class Base(DeclarativeBase):
    __abstract__ = True

    # v1
    # id = Column(
    #     BigInteger,
    #     primary_key=True,
    #     autoincrement=True,
    #     unique=True
    # )

    # v2
    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True,
        unique=True
    )

class User(Base):
    __tablename__ = 'users'

    name: Mapped[str] = mapped_column(
        String(25),  # VARCHAR(25)
        nullable=False  # NOT NULL
    )
    surname: Mapped[str] = mapped_column(
        String(30),
        nullable=True
    )
    username: Mapped[str] = mapped_column(
        String(25),
        nullable=False,
        index=True
    )
    age: Mapped[int] = mapped_column(
        SmallInteger,
        nullable=True
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )
Base.metadata.create_all(engine)

Base = sessionmaker(
    bind=engine,
)