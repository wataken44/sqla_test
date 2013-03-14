#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" tutorial_declarative.py


"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

class DBManager(object):
    def __init__(self):
        self._base = declarative_base()

    def get_base(self):
        return self._base

DBM = DBManager()

class User(DBM.get_base()):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(64))

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "<User(id:%d, name:%s)>" % (self.id, self.name)


def main():
    engine = create_engine('mysql://root@localhost/sqla_test', echo=True)
    
    print(User.__table__)
    print(User.__mapper__)

    DBM.get_base().metadata.create_all(engine)

if __name__ == "__main__":
    main()
