import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    age = Column(String(250))
    followed = Column(String(250), nullable=False)
    followers = Column(String(250), nullable=False)
    email = Column(String(250), unique=True, nullable=False)
    phone = Column(String(250), nullable=False)

class business_Account(Base):
    __tablename__= 'business'
    id = Column(Integer, primary_key=True, unique=True)
    user_business = Column(String(250), nullable=False)
    bussiness_email = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True, unique=True)
    tag = Column(String(250))
    post = Column(String(250), nullable=False)
    likes = Column(String(250))
    comments = Column(String(250))
    location = Column(String(250))
    data =  Column(String(250), nullable=False)
    status = Column(String(64), default='pending')
    user_id = Column(Integer, ForeignKey('user.id'))
    business_id = Column(Integer, ForeignKey('business.id'))
    user = relationship(User)
    user = relationship( business_Account)

class Media(Base):
    __tablename__ = 'media'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True, unique=True)
    type = Column(String(250), nullable=False)
    Comments = Column(String(250))
    user_id = Column(Integer, ForeignKey('post.id'))
    user = relationship(Post)

class Comments(Base):
    __tablename__ = 'comments'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True, unique=True)
    data = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
