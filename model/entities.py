from sqlalchemy import Column, Integer, String, Sequence, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from database import connector

class Career(connector.Manager.Base):
    __tablename__ = 'careers'
    id_career = Column(Integer, Sequence('career_id_seq'), primary_key=True)
    name_career = Column(String(50))

class Subject(connector.Manager.Base):
    __tablename__ = 'subjects'
    id_subject = Column(Integer, Sequence('subject_id_seq'), primary_key=True)
    name_subject = Column(String(100))
    career_from_id = Column(Integer, ForeignKey('careers.id_career'))

class User(connector.Manager.Base):
    __tablename__ = 'users'
    id_user = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name_user = Column(String(250))
    lastname = Column(String(250))
    password = Column(String(30))
    email = Column(String(255))
    career_from_id = Column(Integer, ForeignKey('careers.id_career'))

class Question(connector.Manager.Base):
    __tablename__ = 'questions'
    id_question = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    user_from_id=Column(Integer, ForeignKey('users.id_user'))
    question = Column(String(250))
    description = Column(String(1200))
    score = Column(Integer)
    question_date = Column(default=datetime.now())

class Answer(connector.Manafiger.Base):
    __tablename__ = 'answers'
    id_answer = Column(Integer, Sequence('post_id_seq'), primary_key=True)
    user_from_id = Column(Integer, ForeignKey('users.id_user'))
    question_from_id = Column(Integer, ForeignKey('questions.id_question'))
    answer = Column(String(1500))
    question_date = Column(default=datetime.now())
    score = Column(Integer)
    #star = Column(Boolean(create_constraint=False))

