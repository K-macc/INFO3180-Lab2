from app import app
from flask import render_template, request, redirect, url_for, flash
import datetime


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)

@app.route('/profile')
def profile():
    
    user_info = {
        "Name": "Keshawn McGrath",
        "Username": "@k_mac",
        "Location": "Kingston, Jamaica",
        "Date_Joined": format_date_joined(2025, 2, 26),
        "Bio": "I am a 22-year-old Computer Science major in my third year of study. Hailing from the vibrant city of Montego Bay, I am a proud alumnus of Cornwall College. Currently serving as the Hall Chairman of Taylor Hall, I demonstrate strong leadership skills alongside my academic pursuits, embodying a balance of dedication both in and out of the classroom.",
        "Posts": 7,
        "Following": 1270,
        "Followers": 1185
        
    }
    
    return render_template('profile.html', user=user_info)


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


def format_date_joined(y,m,d):
    date_joined = datetime.date(y,m,d)
    return "Joined " + date_joined.strftime('%B, %Y')
