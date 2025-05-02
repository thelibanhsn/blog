from flask import Blueprint
from ..extensions import FlaskForm, db, bcrypt, login_manager, login_user, logout_user, current_user, login_required
from flask import render_template, redirect, url_for, flash, request
from .forms import UserRegistrationForm, UserLoginForm
from .models import User

auth_bp = Blueprint('auth_bp', __name__, url_prefix='/auth', template_folder='templates')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = UserRegistrationForm()
    if form.validate_on_submit():
        # check if user's username and email already exists
        existing_user = User.query.filter((User.username == form.username.data) | (User.email == form.email.data)).first()
        if existing_user:
            flash('Username or email already exists. Please try again.', 'danger')
            return redirect(url_for('auth_bp.user_register'))
        # hash the password and create a new user  
        print(form.name.data)
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        new_user = User(name= form.name.data, username=form.username.data, email=form.email.data, password=hashed_password)
        print(new_user)
        User.save(new_user)
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('auth_bp.login'))
    return render_template('register.html', form=form)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = UserLoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard_bp.index'))
        else:
            flash('Invalid username or password. Please try again.', 'danger')
    return render_template('login.html', form=form)


# logout
@auth_bp.route('/logout/')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('auth_bp.login'))


