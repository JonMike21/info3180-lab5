# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from wtforms import StringField, FileField, TextAreaField, SelectField, DateField
from wtforms.validators import InputRequired
from flask_wtf.file import  FileRequired, FileAllowed

class MovieForm(FlaskForm):
    title= StringField('Title', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    poster = FileField('Poster', validators=[FileRequired(),FileAllowed(['jpg', 'png','jpeg','JPG'], 'Images only!')])    
    #created_at = DateField('Created_at', format='%m/%d/%Y', validators=[InputRequired()])
