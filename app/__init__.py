import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from . import testdata

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    # Temporary images. TODO replace with actual images.
    photos = ['hamster.png', 'hamster.png', 'hamster.png', 'hamster.png', 'hamster.png']
    locations = [
        {"name": "New York", "lat": 40.7128, "lng": -74.0060, "visited_by": "Hamster"},
        {"name": "San Francisco", "lat": 37.7749, "lng": -122.4194, "visited_by": "Ebony"},
        {"name": "Pennsylvania", "lat": 13.847161255761124, "lng":100.39281811647348 , "visited_by": "Ebony"},
        {"name": "Boston", "lat": 42.3601, "lng": -71.0589, "visited_by": "Hamster"},
    ]

    # TODO fill in actual about sections.
    abouts = [
        {
            'title': 'About Hamster',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean commodo mi vel mauris iaculis placerat. Maecenas suscipit ipsum massa. Proin.'
        },
        {
            'title': 'About Ebony Brown',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean commodo mi vel mauris iaculis placerat. Maecenas suscipit ipsum massa. Proin.'
        }
    ]
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), photos=photos, abouts=abouts, locations=locations)

@app.route('/resume')
def resume():
    return render_template('resume.html', title="Work Experience", exp=testdata.workData, edu=testdata.schoolData, url=os.getenv("URL"))

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', title="Hobbies", hobbies=testdata.hobbiesData)
