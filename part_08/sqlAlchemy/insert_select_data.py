# Create a session to interact with the database
from sqlalchemy.orm import sessionmaker

from part_08.sqlAlchemy.main import User, engine

Session = sessionmaker(bind=engine)
session = Session()

# Add a user to the database
user = User(name='John Doe', age=30)
session.add(user)
session.commit()

# Query the database
users = session.query(User).all()
for user in users:
    print(f'User {user.id}: {user.name}, {user.age} years old')
