import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from . import testdata

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/resume')
def resume():
    return render_template('resume.html', title="Work Experience", exp=testdata.workData, edu=testdata.schoolData, url=os.getenv("URL"))