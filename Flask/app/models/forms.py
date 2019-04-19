from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField, RadioField, IntegerField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField("username", validators = [DataRequired()])
    password = PasswordField("password", validators = [DataRequired()])

#INSERT INTO users (username, password,admin ) VALUES ("lucas", "123", 1)

class RegisterForm(FlaskForm):
    username = StringField("username", validators = [DataRequired()])
    password = PasswordField("password", validators = [DataRequired()])
    password2 = PasswordField("password2", validators = [DataRequired()])
    admin = BooleanField("admin", validators = [DataRequired()])
