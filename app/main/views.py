from flask import render_template
from . import main

# views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to The best Pitch website Online '
    return render_template('index.html',title = title )


@main.route('/Pitch/<int:pitch_id>')
def pitch(pitch_id):
    '''
    View pitch page function that returns the pitch details page and its data
    '''
    return render_template('pitch.html',id = pitch_id)
