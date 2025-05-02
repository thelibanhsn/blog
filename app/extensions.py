from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user, login_required
from flask_wtf import FlaskForm
from wtforms import StringField,  PasswordField, SelectField, SubmitField, EmailField, TextAreaField
from wtforms.validators import DataRequired, Length
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt


db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()
data_required = DataRequired()
bcrypt = Bcrypt()