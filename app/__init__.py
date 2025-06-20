import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    # Temporary images. TODO replace with actual images.
    photos = ['David Benjamin.jpg', 'David Benjamin.jpg', 'David Benjamin.jpg', 'David Benjamin.jpg', 'David Benjamin.jpg']
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), photos=photos)
