from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

from My_CW.SQLAlchemy_4.lesson_2.db_connector import DBConnector
from My_CW.SQLAlchemy_4.lesson_2.social_blogs_models import *

engine = create_engine(
    url="mysql+pymysql://ich1:ich1_password_ilovedbs@ich-edit.edu.itcareerhub.de:3306/social_blogs",
    echo=True,
    future=True
)


# Session = sessionmaker(bind=engine)
# session = Session()
# session.close()


with DBConnector(engine) as session:
    # CRUD operations

    # C (Create)
    data = {"name": "NewRole"}

    new_role = Role(**data)*data)