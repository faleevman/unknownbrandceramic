import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'

    uid = Column(Integer, primary_key=True)
    role = Column(Integer, nullable=False)
    balance = Column(Integer, nullable=False)
    username = Column(String)

class NFT(Base):
    __tablename__ = 'nft'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    description = Column(String(250), nullable=False)
    pricePlace = Column(String(250), nullable=False)
    pricePerDay = Column(String(250), nullable=False)

engine = create_engine("sqlite:///db.sqlite")
Base.metadata.create_all(engine)
