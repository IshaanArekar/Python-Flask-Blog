from flak_wtf import FlaskForm
from wtforms import StringField 
from wtforms.validators import DataRequired , length

class RegistrationForm(FlaskForm):
    Username = StringField('Username', validators = [DataRequired(), length(min = 2, max = 20) ])

    

