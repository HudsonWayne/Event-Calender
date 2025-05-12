from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateTimeLocalField, SubmitField
from wtforms.validators import DataRequired



class EventForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    start = DateTimeLocalField('Start Time', format='%Y-%m-%dT%H:%M', validators=[DataRequired()])
    end = DateTimeLocalField('End Time', format='%Y-%m-%dT%H:%M')