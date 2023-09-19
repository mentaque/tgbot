from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_engine = create_engine('sqlite:///mydatabase.db')  # Замените на имя вашей базы данных
Session = sessionmaker(bind=db_engine)
session = Session()
