from flask_app import app
from flask_app.models.user import User
from flask import render_template, request, redirect, session

@app.route('/')
def login_register():
    if 'user_id' in session: 
        return redirect('/dashboard')
    return render_template("index.html")


@app.route('/register' , methods = ['POST'])
def register():
    if User.register_validation(request.form):
        User.create(request.form)
    return redirect('/')


@app.route('/login' , methods=['POST'])
def login():
    data = request.form
    if User.login_validation(data):
        session['logged_user_email'] = data['email']
        return redirect('/dashboard')
    return redirect('/')       

@app.route('/dashboard')
def dashboard():
    logged_user = User.get_by_email({'email': session['logged_user_email']})
    return render_template("dashboard.html", logged_user = logged_user)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')