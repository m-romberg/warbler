"""Seed database with sample data from CSV Files."""

from csv import DictReader
from app import db
from models import User, Message, Follows, Likes, DEFAULT_HEADER_IMAGE_URL, DEFAULT_IMAGE_URL

db.drop_all()
db.create_all()

with open('generator/users.csv') as users:
    db.session.bulk_insert_mappings(User, DictReader(users))

with open('generator/messages.csv') as messages:
    db.session.bulk_insert_mappings(Message, DictReader(messages))

with open('generator/follows.csv') as follows:
    db.session.bulk_insert_mappings(Follows, DictReader(follows))

user1 = User(username='Vaughn', email='vseekamp@gmail.com', image_url=DEFAULT_IMAGE_URL, header_image_url=DEFAULT_HEADER_IMAGE_URL, bio='Yo', password='password')
user2 = User(username='Madelyn', email='madelyn@gmail.com', image_url=DEFAULT_IMAGE_URL, header_image_url=DEFAULT_HEADER_IMAGE_URL, bio='Hi', password='password')

like1 = Likes(user_id=1, message_id=1)
like2 = Likes(user_id=2, message_id=2)
like3 = Likes(user_id=3, message_id=3)
like4 = Likes(user_id=1, message_id=5)
like5 = Likes(user_id=4, message_id=4)

db.session.add_all([like1, like2, like3, like4, like5, user1, user2])


db.session.commit()
