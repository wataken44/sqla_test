#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" tutorial_session.py


"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

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

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "<User(id:%d, name:%s)>" % (self.id, self.name)

def main():
    DBM.setup()
    session = DBM.create_session()
    
    u1 = User('User4')
    session.add(u1)
    u1.name = 'User5'
    print(session.dirty)

    first_user = session.query(User).filter_by(name='User4').first()
    print(first_user)
    print(u1 == first_user)
    print(session.dirty)
    print(session.new)
    print(u1.name)

    session.commit()
    print("# committed")
    print(session.dirty)
    print(u1.name)

if __name__ == "__main__":
    main()
