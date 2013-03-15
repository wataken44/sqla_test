#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" tutorial_relationship.py


"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship, sessionmaker

class DBManager(object):
    def __init__(self, database_uri, echo=False):
        self._engine = create_engine(database_uri, echo=echo)
        self._base = declarative_base()
        self._session = sessionmaker(bind = self._engine)

    def get_engine():
        return self._engine

    def get_base(self):
        return self._base

    def create_session(self):
        return self._session(autocommit=False, autoflush=False)

    def setup(self):
        self._base.metadata.create_all(self._engine)

DBM = DBManager('mysql://root@localhost/sqla_test', echo=True)

class User(DBM.get_base()):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    addresses = relationship("Address")

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "<User(id:%d, name:%s)>" % (self.id, self.name)

class Address(DBM.get_base()):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email_address = Column(String(256), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    def __init__(self, email_address):
        self.email_address = email_address

    def __repr__(self):
        return "<Address('%s')>" % self.email_address

def main():
    DBM.setup()
    session = DBM.create_session()
    
    u1 = User('User4')
    print(u1.addresses)
    u1.addresses = [
        Address('User4@gmail.com'), Address('wataken44@example.com')]

    session.add(u1)

    session.flush()
    session.commit()


if __name__ == "__main__":
    main()
