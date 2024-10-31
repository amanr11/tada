from flask import Blueprint, request, render_template,flash, redirect, url_for
from .models import Assessment
from .forms import AssessmentForm
from . import db
from datetime import datetime

main = Blueprint('main', __name__)

# Route for homepage to view all assessments
@main.route('/')
def index():
    assessments = Assessment.query.order_by(Assessment.deadline_date.asc()).all()
    form = AssessmentForm()  # Create an instance of your form
    return render_template('index.html', assessments=assessments, form=form)

# Route to view only uncompleted assessments
@main.route('/assessments/uncompleted')
def view_uncompleted_assessments():
    assessments = Assessment.query.filter_by(is_complete=False).all()
    form = AssessmentForm()
    return render_template('view_uncompleted.html', assessments=assessments, form = form)

# Route to view only completed assessments
@main.route('/assessments/completed')
def view_completed_assessments():
    assessments = Assessment.query.filter_by(is_complete=True).all()
    form = AssessmentForm()
    return render_template('view_completed.html', assessments=assessments, form=form)

@main.route('/add', methods=['GET', 'POST'])
def add_assessment():
    form = AssessmentForm()
    if request.method == 'GET':
        title = request.args.get('title', '')
        form.title.data = title  # Pre-fill the title field
    
    if form.validate_on_submit():
        new_assessment = Assessment(
            title=form.title.data,
            module_code=form.module_code.data,
            deadline_date=form.deadline_date.data,
            description=form.description.data,
            is_complete=form.is_complete.data
        )
        db.session.add(new_assessment)
        db.session.commit()
        flash('assessment added successfully!', 'success')  # Flash message
        return redirect(url_for('main.index'))
    
    return render_template('add_assessment.html', form=form)


@main.route('/edit/<int:assessment_id>', methods=['GET', 'POST'])
def edit_assessment(assessment_id):
    assessment = Assessment.query.get_or_404(assessment_id)
    form = AssessmentForm(obj=assessment)
    if form.validate_on_submit():
        assessment.title = form.title.data
        assessment.module_code = form.module_code.data
        assessment.deadline_date = form.deadline_date.data
        assessment.description = form.description.data
        assessment.is_complete = form.is_complete.data
        db.session.commit()
        flash('assessment updated successfully!', 'success')  # Flash message
        return redirect(url_for('main.index'))
    return render_template('edit_assessment.html', form=form, assessment=assessment)

@main.route('/delete/<int:assessment_id>', methods=['POST'])
def delete_assessment(assessment_id):
    assessment = Assessment.query.get_or_404(assessment_id)
    db.session.delete(assessment)
    db.session.commit()
    flash('assessment deleted successfully!', 'danger')  # Flash message
    return redirect(url_for('main.index'))

#Route to mark an assesment as complete
@main.route('/complete/<int:assessment_id>', methods=['POST'])
def mark_as_complete(assessment_id):
    assessment = Assessment.query.get_or_404(assessment_id)
    assessment.is_complete = True
    db.session.commit()
    return redirect(url_for('main.index'))

# Route to view details of a specific assessment
@main.route('/assessment/<int:assessment_id>')
def view_assessment(assessment_id):
    assessment = Assessment.query.get_or_404(assessment_id)
    form = AssessmentForm()
    return render_template('view_assessment.html', assessment=assessment, form=form)

#Route to add assessments directly from homepage
@main.route('/add_assessment_from_homepage', methods=['POST'])
def add_assessment_from_homepage():
    form = AssessmentForm()
    if form.validate_on_submit():
        new_assessment = Assessment(
            title=form.title.data,
            module_code=form.module_code.data,
            deadline_date=form.deadline_date.data,
            description=form.description.data,
            is_complete=False  # Assuming new assessments are not completed by default
        )
        db.session.add(new_assessment)
        db.session.commit()
        flash('assessment added successfully!', 'success')
        return redirect(url_for('main.index'))
    return redirect(url_for('main.index'))