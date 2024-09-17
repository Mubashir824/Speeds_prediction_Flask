# forms.py

from flask_wtf import FlaskForm
from wtforms import IntegerField, FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class DataEntryForm(FlaskForm):
    year = IntegerField('Year', validators=[DataRequired(), NumberRange(min=2022, max=2100)])
    month = IntegerField('Month', validators=[DataRequired(), NumberRange(min=1, max=12)])
    day = IntegerField('Day', validators=[DataRequired(), NumberRange(min=1, max=31)])
    hour = IntegerField('Hour', validators=[DataRequired(), NumberRange(min=0, max=23)])
    minute = IntegerField('Minute', validators=[DataRequired(), NumberRange(min=0, max=59)])
    temperature = FloatField('Temperature', validators=[DataRequired()])
    humidity = FloatField('Humidity', validators=[DataRequired(), NumberRange(min=0, max=100)])
    submit = SubmitField('Submit')