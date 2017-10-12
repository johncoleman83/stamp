#!/usr/bin/python3
"""
Image Class from Models Module
"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey,\
    MetaData, Table, ForeignKey
from sqlalchemy.orm import backref


class Image(BaseModel, Base):
    """Place class handles all application places"""
    __tablename__ = 'images'
    url = Column(String(512), nullable=False)
    title = Column(String(256), nullable=True)
    description = Column(String(1024), nullable=True)
    family = Column(String(256), nullable=True)
    collection = Column(String(200), nullable=True)
    users = relationship('User', secondary="user_images",
                         viewonly=False)
    user_images = relationship('UserImage',
                               backref='images',
                               cascade='delete')
