from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SubmitField, DateField
from wtforms.validators import DataRequired, Length, ValidationError
from datetime import date

class AssessmentForm(FlaskForm):
    title = StringField('title', validators=[
        DataRequired(), 
        Length(min=3, message='title must be at least 3 characters long.')
    ])
    module_code = StringField('module code', validators=[DataRequired()])
    deadline_date = DateField('deadline date', format='%Y-%m-%d', validators=[DataRequired()])
    description = TextAreaField('description', validators=[
        Length(max=200, message='description must be 200 characters or less.')
    ])
    is_complete = BooleanField('completed? ')
    submit = SubmitField('done')

    def validate_deadline_date(self, deadline_date):
        if deadline_date.data < date.today():
            raise ValidationError('deadline must be a future date.')
