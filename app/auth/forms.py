from ..extensions import FlaskForm, StringField, SubmitField, data_required, Length, EmailField, PasswordField

class UserLoginForm(FlaskForm):
    email = StringField('Email', validators=[data_required, Length(min=3, max=50)])
    password = PasswordField('Password', validators=[data_required, Length(min=4, max=50)])
    submit = SubmitField('Login')

class UserRegistrationForm(FlaskForm):
    name = StringField('Name',validators=[data_required,Length( max=50)])
    username = StringField('Username',validators=[data_required,Length( max=50)])
    email = EmailField('Email',validators=[data_required,Length( max=50)])
    password = PasswordField('Password',validators=[data_required,Length( max=32)])
    submit = SubmitField('Register')