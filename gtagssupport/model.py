#-*- coding:utf-8 -*-

import sqlalchemy as sql
from sqlalchemy import orm
from sqlalchemy.ext import declarative as decl

Base = decl.declarative_base()


class Entry(Base):

    __tablename__ = 'entry'
    
    declname = decl.Column(sql.String(255), primary_key=True)
    lineno = decl.Column(sql.Integer, primary_key=True)
    file = decl.Column(sql.String(255), primary_key=True)
    line = decl.Column(sql.String(512))


class Session():

    def __init__(self):

        self.session = session()


    def __enter__(self):

        return self.session


    def __exit__(self, *exception):

        if exception[0] is not None:
            self.session.rollback()
        else:
            self.session.commit()

        self.session.close()
    

def initialize(root):

    global engine
    global session
    global meta

    path = 'sqlite:///%s.gtagscache.db' % root
    print path
    engine = sql.create_engine(path)

    session = orm.sessionmaker()
    session.configure(bind=engine)

    Base.metadata.bind = engine
    Base.metadata.create_all()


