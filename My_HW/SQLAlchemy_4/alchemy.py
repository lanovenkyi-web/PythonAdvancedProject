from sqlalchemy import create_engine, String, Boolean, ForeignKey, select, Numeric,func
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, relationship, mapped_column, joinedload
from pathlib import Path

BASE_DIR = Path(__file__).parents[2]
print(__file__)
print(BASE_DIR)

engine = create_engine(
    url=f"sqlite:///{BASE_DIR / 'My_DataBase.db'}"
)


class Base(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)


class Category(Base):
    __tablename__ = 'Category'

    name: Mapped[str] = mapped_column(
        String(100), nullable=True)

    description: Mapped[str] = mapped_column(
        String(255), nullable=True)

    products = relationship("Products", back_populates="category")


class Products(Base):
    __tablename__ = 'Product'

    name: Mapped[str] = mapped_column(
        String(100), nullable=False)

    price: Mapped[Numeric] = mapped_column(
        Numeric(), nullable=True)

    is_stock: Mapped[bool] = mapped_column(
        Boolean, default=True
    )

    category_id: Mapped[int] = mapped_column(ForeignKey("Category.id"), nullable=True)

    category = relationship("Category", back_populates="products")



Base.metadata.create_all(bind=engine)
Session = sessionmaker(
    bind=engine
)
#-----------Очистка-------------------
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
#------------------------------
session = Session()
electronics = Category(name='Electronics', description='Gadgets and devices')
books = Category(name='Books', description='Printed books and e-books')
clothing = Category(name='Clothing', description='Clothing for men and women')

session.add_all([electronics, books, clothing])
session.commit()

session.add_all([

Products(name='Smartphone', price=299.99, is_stock=True, category=electronics),
Products(name='Laptop', price=499.99, is_stock=True, category=electronics),
Products(name='Science fiction novel', price=15.99, is_stock=True, category=books),
Products(name='Jeans', price=40.50, is_stock=True, category=clothing),
Products(name='T-shirt', price=20.00, is_stock=True, category=clothing)
])
session.commit()
print("Данные успешно добавлены в базу")


categories = session.scalars(select(Category)).all()

for c in categories:
    print(c.id, c.name, c.description)


# -------------------------------------------------------------------------------------------
with Session() as session:
    stmt = (
        select(Category)
        .options(joinedload(Category.products))
    )
    result = session.scalars(stmt).unique().all()

    for cat in result:
        print(f"Категория: {cat.name}")
        for prod in cat.products:
            print(f"  -- Продукт: {prod.name}, Цена: {prod.price}")

# -------------------------------------------------------------------------------------------
product = session.get(Products, 1)
if product:
    product.price = 349.99
    session.commit()
product = session.get(Products, 1)
if product:
    print(product.name, product.price)
#--------------------------------------------------------------------------------------------

with Session() as session:
    stmt = (
        select(
            Category.name,
            func.count(Products.id)
        )
        .join(Products)
        .group_by(Category.id)

    )

    result = session.execute(stmt)

    for name, count in result:
        print(f"{name}: {count}")

    session.commit()
#-----------------------------------------------------------------------------------------------

with Session() as session:
    stmt = (
        select(
            Category.name,
            func.count(Products.id)
        )
        .join(Products)
        .group_by(Category.id)
        .having(func.count(Products.id) > 1)

    )

    result = session.execute(stmt)

    for name, count in result:
        print(f"Категории, с количеством товара более одного: {name}: {count}")

    session.commit()