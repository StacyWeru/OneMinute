from flask import render_template 
from app import main 
from .forms import LoginForm

# @main.route('/')
# def index():

@main.route('/login')
def login():
    form = LoginForm()
    return render_template ('login.html' , title = 'Sign In' , form=form)