# coding: utf-8
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, BigInteger, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Amigo(Base):
    __tablename__ = 'amigo'
    __table_args__ = (UniqueConstraint('latitude', 'longitude', name='localizacao'),)
    id = Column(BigInteger().with_variant(Integer, "sqlite"), primary_key=True)
    nome = Column(String(250), nullable=False)
    longitude = Column(Integer)
    latitude = Column(Integer)

engine = create_engine('sqlite:///db/desafio.db')
Base.metadata.create_all(engine)
