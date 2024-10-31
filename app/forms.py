from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SubmitField, DateField
from wtforms.validators import DataRequired, Length, ValidationError
from datetime import date
from .models import Assessment
import re

class AssessmentForm(FlaskForm):
    title = StringField('title', validators=[
        DataRequired(), 
        Length(min=3, max=35, message='Title must be between 3 and 35 characters long.')
    ])
    module_code = StringField('module code', validators=[
        DataRequired(), 
        Length(max=10, message='Module code must be 10 characters or less.')
    ])
    deadline_date = DateField('deadline date', format='%Y-%m-%d', validators=[DataRequired()])
    description = TextAreaField('description', validators=[
        Length(max=200, message='Description must be 200 characters or less.')
    ])
    is_complete = BooleanField('completed? ')
    submit = SubmitField('done')

    def validate_deadline_date(self, deadline_date):
        if deadline_date.data <= date.today():
            raise ValidationError('Deadline must be a future date.')
    
    def validate_title(self, title):
        existing_assessment = Assessment.query.filter_by(title=title.data).first()
        if existing_assessment:
            raise ValidationError('this title already exists. please choose a different title.')
        
    def validate_title(self, title):
        if not re.match(r'^[A-Za-z0-9\s.,\'"]+$', title.data):
            raise ValidationError('title contains invalid characters. only letters, numbers, spaces, and basic punctuation are allowed.')

    def validate_module_code(self, module_code):
        if not re.match(r'^[A-Za-z0-9\s]+$', module_code.data):
            raise ValidationError('module code contains invalid characters. only letters, numbers, and spaces are allowed.')

