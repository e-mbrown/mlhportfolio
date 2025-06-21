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
    # TODO fill in actual about sections.
    abouts = [
        {
            'title': 'About David Benjamin',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean commodo mi vel mauris iaculis placerat. Maecenas suscipit ipsum massa. Proin.'
        },
        {
            'title': 'About Ebony Brown',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean commodo mi vel mauris iaculis placerat. Maecenas suscipit ipsum massa. Proin.'
        }
    ]
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), photos=photos, abouts=abouts)

@app.route('/resume')
def resume():
    return render_template('resume.html', title="Work Experience", exp=testdata.workData, edu=testdata.schoolData, url=os.getenv("URL"))

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', title="Hobbies", hobbies=testdata.hobbiesData)