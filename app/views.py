from app import app
from flask import render_template
from datetime import date

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


def format_date_joined(d):
    return d.strftime("%B, %Y")  # "February, 2021"


@app.route('/profile')
def profile():
    import os
    print("ROOT:", app.root_path)
    print("TEMPLATES:", os.listdir(os.path.join(app.root_path, "templates")))

    joined_raw = date(2021, 2, 1)
    joined_formatted = format_date_joined(joined_raw)

    return render_template(
        "profile.html",
        full_name="Mary Jane",
        username="mjane",
        location="Kingston, Jamaica",
        joined=joined_formatted,
        bio=("I am a smart and talented young woman who loves website design "
             "and development. Contact me if you'd like to work together on a new project."),
        posts=7,
        following=100,
        followers=250
    )

###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404