"""Seed database with sample data from CSV Files."""

from csv import DictReader
from app import db
from models import User, Message, Follows, Likes

db.drop_all()
db.create_all()

with open('generator/users.csv') as users:
    db.session.bulk_insert_mappings(User, DictReader(users))

with open('generator/messages.csv') as messages:
    db.session.bulk_insert_mappings(Message, DictReader(messages))

with open('generator/follows.csv') as follows:
    db.session.bulk_insert_mappings(Follows, DictReader(follows))

# like1 = Likes(1, 20)
# like2 = Likes(2,30)
# like3 = Likes(301,40)
# like4 = Likes(301,60)
# like5 = Likes(301,30)

# db.session.add_all([like1, like2, like3, like4, like5])


db.session.commit()
