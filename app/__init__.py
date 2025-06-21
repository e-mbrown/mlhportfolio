import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from . import testdata

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
# Temporary images. TODO replace with actual images.
    photos = ['David Benjamin.jpg', 'David Benjamin.jpg', 'David Benjamin.jpg', 'David Benjamin.jpg', 'David Benjamin.jpg']
    locations = [
        {"name": "New York", "lat": 40.7128, "lng": -74.0060, "visited_by": "David"},
        {"name": "San Francisco", "lat": 37.7749, "lng": -122.4194, "visited_by": "Ebony"},
        {"name": "Boston", "lat": 42.3601, "lng": -71.0589, "visited_by": "David"},
    ]
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), photos=photos, locations=locations)

@app.route('/resume')
def resume():
    return render_template('resume.html', title="Work Experience", exp=testdata.workData, edu=testdata.schoolData, url=os.getenv("URL"))
