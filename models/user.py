import sqlite3
from db import db
from flask import flash
import datetime

from sqlalchemy import  DateTime

class UserModel(db.Model):
    __tablename__ = 'paidusers'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(260),unique=True)
    password = db.Column(db.String(80))

    is_active = db.Column(db.Boolean, unique=False, default=True)
    created_date = db.Column(DateTime, default=datetime.datetime.utcnow())

    def __init__(self, username, email,password):
        self.username = username
        self.email=email
        self.password = password
        self.is_active=True


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        delete_this=cls.query.filter_by(username=username).first()
        if delete_this is not None:
            someday=datetime.datetime.utcnow()
            actual=delete_this.created_date
            j=someday - actual
            if j.days>28:
                db.session.delete(delete_this)
                db.session.commit()
            return cls.query.filter_by(username=username).first()


        return cls.query.filter_by(username=username).first()


    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()


    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
