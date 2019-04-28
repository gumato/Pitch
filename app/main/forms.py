from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, SelectField, RadioField
from wtforms.validators import Required

class CommentsForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[Required()])
    vote=RadioField('default field arguments', choices=[('1', 'UpVote'), ('1', 'DownVote')])
    submit = SubmitField('SUBMIT')

class PitchForm(FlaskForm):
    category_id = SelectField('Select Category', choices=[('1', 'Technology Pitch'), ('2', 'Business Pitch'), ('3', 'Promotion Pitch'),('4','Interview Pitch'),('5','Production Pitch')])
    content = TextAreaField('YOUR PITCH')
    submit = SubmitField('Create Pitch')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class UpvoteForm(FlaskForm):
    '''
    Class to create a wtf form for upvoting a pitch
    '''
    submit = SubmitField('Upvote')
