from app import db
import datetime


class Income(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    income = db.Column(db.Float)
    incometime = db.Column(db.String(500))


class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    expense = db.Column(db.Float)
    expensetime = db.Column(db.String(500))
