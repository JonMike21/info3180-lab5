"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from flask import render_template, request, jsonify, send_file,  redirect, url_for, flash, session, abort,send_from_directory
import os
from app.models import movies
from app.forms import MovieForm
from app import app,db
from werkzeug.utils import secure_filename
import datetime
from flask_wtf.csrf import generate_csrf


###
# Routing for your application.
###

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")


@app.route('/api/v1/movies', methods=['POST'])
def get_movies():
    form=MovieForm()
    if form.validate_on_submit:
        title= form.title.data
        description= form.description.data
        posterdata= form.poster.data
        poster= secure_filename(posterdata.filename)
        posterdata.save(os.path.join(app.config['UPLOAD_FOLDER'],poster))
        
        #created_at= form.created_at.data
        created_at=datetime.datetime.now()

        new_movie = movies(title,description,poster,created_at)
        db.session.add(new_movie)
        db.session.commit()        

        moviee={
            'message': 'Movie Successfully added',
            'poster': poster,
            'description': description,
            'created_at': created_at
        }
        return jsonify(moviee)

        #return jsonify(message='Movie Successfully added',poster=poster,description=description,created_at=created_at)
    
    
    return jsonify(errors=form_errors(form))

@app.route('/api/v1/csrf-token', methods=['GET'])
def get_csrf():
 return jsonify({'csrf_token': generate_csrf()})
        


     




###
# The functions below should be applicable to all Flask apps.
###

# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404