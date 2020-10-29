import uuid
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

path = "sqlite:///sochi_athletes.sqlite3"
base = declarative_base()

engine = sa.create_engine(path)
base.metadata.create_all(engine)
session_ = sessionmaker(engine)
session = session_()

class User(base):
	__tablename__ = 'user'
	id = sa.Column(sa.String(36), primary_key=True)
	first_name = sa.Column(sa.Text)
	last_name = sa.Column(sa.Text)
	gender = sa.Column(sa.Text)
	email = sa.Column(sa.Text)
	birthdate = sa.Column(sa.Text)
	height = sa.Column(sa.Float)

def registration():
	first_name = input("Name: ")
	last_name = input("Surname: ")
	gender = input("Gender: ")
	email = input("Email: ")
	birthdate = input("Birthday: ")
	height = input("Height: ")
	user_id = str(uuid.uuid4())
	user = User(
		id = user_id,
		first_name = first_name,
		last_name = last_name,
		gender = gender,
		email = email,
		birthdate = birthdate,
		height = height)
	return user

def main():
	session.add(registration())
	session.commit()

if __name__ == "__main__":
    main()