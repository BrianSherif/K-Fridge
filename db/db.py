from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# class user():
#     userid = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(120), unique=False, nullable=False)
#     items = db.Column(db.String(256), unique=False, nullable=False)

#     def __repr__(self):
#         return '<user %r>' % self.username

