import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

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
