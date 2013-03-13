#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" tutorial_connect.py


"""

import sqlalchemy
from sqlalchemy import create_engine

def main():
    print(sqlalchemy.__version__)

    engine = create_engine('mysql://root@localhost/sqla_test', echo=True)

    print(engine.execute("select 1").scalar())

if __name__ == "__main__":
    main()
