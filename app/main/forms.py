from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField,SelectField
from wtforms.validators import Required,Email,EqualTo
from ..models import User
from wtforms import ValidationError

class UpdateProfile(FlaskForm):
    bio = TextAreaField('ABOUT YOU' , validators=[Required()])
    submit = SubmitField('SUBMIT')

class PitchForm(FlaskForm):
    title=StringField("welcome to Pitch Ideas")
    Pitch_category = SelectField('Pitch Category',choices=[('Technology-Pitch','Technology Pitch'),('Business-Pitch,Business Pitch'),('Promotion-Pitch,Promotion Pitch'),('Interview-Pitch,Interview pitch'),('Product-Pitch,Product Pitch')],validators=[Required()])
    content = TextAreaField('YOUR PITCH')
    submit = SubmitField('SUBMIT')

class CommentForm(FlaskForm):

    comment_id = TextAreaField('WRITE COMMENT')
    submit = SubmitField('SUBMIT')

class CategoriesForm(FlaskForm):
    name =  TextAreaField('PITCH')
    submit = SubmitField('SUBMIT')
