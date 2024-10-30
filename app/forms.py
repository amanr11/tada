from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SubmitField, DateField
from wtforms.validators import DataRequired, Length, ValidationError
from datetime import date

class AssessmentForm(FlaskForm):
    title = StringField('Title', validators=[
        DataRequired(), 
        Length(min=3, message='Title must be at least 3 characters long.')
    ])
    module_code = StringField('Module Code', validators=[DataRequired()])
    deadline_date = DateField('Deadline Date', format='%Y-%m-%d', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[
        Length(max=200, message='Description must be 200 characters or less.')
    ])
    is_complete = BooleanField('Complete')
    submit = SubmitField('Submit')

    def validate_deadline_date(self, deadline_date):
        if deadline_date.data < date.today():
            raise ValidationError('Deadline must be a future date.')
