from flask import render_template, flash
from app import app, db, models
from .forms import ExpenditureForm
from .forms import IncomeForm
from sqlalchemy import desc

@app.route('/')
def index():

    totalIncome = 0
    for item in models.Income.query.all():
        totalIncome = totalIncome + item.income
    totalExpense = 0
    for item in models.Expense.query.all():
        totalExpense = totalExpense + item.expense
    total = totalIncome-totalExpense

    incomes = models.Income.query.order_by(desc(models.Income.incometime)).all()
    expenses = models.Expense.query.order_by(desc(models.Expense.expensetime)).all()

    return render_template('index.html', total = total, totalIncome = totalIncome, totalExpense = totalExpense, incomes=incomes, expenses=expenses)

@app.route('/add', methods=['GET', 'POST'])
def add():
    form1 = IncomeForm()
    if form1.validate_on_submit():
        p = models.Income(income=form1.income.data, incometime=form1.incometime.data)
        if(p.income != None):
            db.session.add(p)
            db.session.commit()
    form2 = ExpenditureForm()      
    if form2.validate_on_submit():
        q = models.Expense(expense=form2.expense.data, expensetime=form2.expensetime.data)
        if(q.expense != None):
            db.session.add(q)
            db.session.commit()

    incomes = models.Income.query.order_by(desc(models.Income.incometime)).all()
    expenses = models.Expense.query.order_by(desc(models.Expense.expensetime)).all()

    return render_template('add.html', form1=form1, form2=form2, incomes=incomes, expenses=expenses)

@app.route('/savings', methods=['GET', 'POST'])
def savings():
    form1 = IncomeForm()
    if form1.validate_on_submit():
        p = models.Income(income=form1.income.data, incometime=form1.incometime.data)
        if(p.income != None):
            db.session.add(p)
            db.session.commit()
    form2 = ExpenditureForm()      
    if form2.validate_on_submit():
        q = models.Expense(expense=form2.expense.data, expensetime=form2.expensetime.data)
        if(q.expense != None):
            db.session.add(q)
            db.session.commit()

    incomes = models.Income.query.all()
    expenses = models.Expense.query.all()

    return render_template('add.html', form1=form1, form2=form2, incomes=incomes, expenses=expenses)


