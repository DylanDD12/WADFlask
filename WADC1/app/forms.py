from flask_wtf import FlaskForm
from wtforms import FloatField
from wtforms import StringField
from wtforms.validators import DataRequired

class IncomeForm(FlaskForm):
    income = FloatField('income', validators=[DataRequired(message='')])
    incometime = StringField('incomedate', validators=[DataRequired(message='')])

class ExpenditureForm(FlaskForm):
    expense = FloatField('expense', validators=[DataRequired(message='')])
    expensetime = StringField('expensedate', validators=[DataRequired(message='')])


