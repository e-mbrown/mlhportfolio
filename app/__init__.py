import os
import datetime
from flask import Flask, render_template, request
from dotenv import load_dotenv
from . import testdata
from peewee import *
from playhouse.shortcuts import model_to_dict

load_dotenv()
app = Flask(__name__)

if os.getenv("TESTING") == "true":
    print("Running in test mode")
    db = SqliteDatabase("file:memory?mode=memory&cache=shared", uri=True)
else:
    db = MySQLDatabase(
        os.getenv("MYSQL_DATABASE"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        host=os.getenv("MYSQL_HOST"),
        port=3306,
    )

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db

db.connect()
db.create_tables([TimelinePost])

@app.route('/')
def index():
    # Temporary images. TODO replace with actual images.
    photos = ['hamster.png']
    locations = [
        {"name": "New York", "lat": 40.7128, "lng": -74.0060, "visited_by": "Hamster"},
        {"name": "San Francisco", "lat": 37.7749, "lng": -122.4194, "visited_by": "Ebony"},
        {"name": "Pennsylvania", "lat": 13.847161255761124, "lng":100.39281811647348 , "visited_by": "Ebony"},
        {"name": "Boston", "lat": 42.3601, "lng": -71.0589, "visited_by": "Hamster"},
    ]

    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), photos=photos, abouts=testdata.aboutData, locations=locations)

@app.route('/resume')
def resume():
    return render_template('resume.html', title="Work Experience", exp=testdata.workData, edu=testdata.schoolData, url=os.getenv("URL"))

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', title="Hobbies", hobbies=testdata.hobbiesData)

@app.route('/api/timeline_post', methods=['POST'])
def post_timeline_post():
    name = request.form.get('name')
    email = request.form.get('email')
    content = request.form.get('content')
    if not name or name == "":
        return "Invalid name,", 400
    if not content or content == "":
        return "Invalid content,", 400
    if not email or '@' not in email:
        return "Invalid email,", 400
    timeline_post = TimelinePost.create(name=name, email=email, content=content)

    return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods=['GET'])
def get_timeline_post():
    return getPosts()

# Not right but on the right track
@app.route('/api/timeline_post/<name>', methods=['DELETE'])
def rm_timeline_post(name):
    query = TimelinePost.delete().where(TimelinePost.name == name)
    res = query.execute()
    return f"{res} records deleted.\n"

@app.route('/timeline')
def timeline():
    posts = getPosts()
    return render_template('timeline.html', title="Timeline", posts=posts['timeline'])



# 
def getPosts():
    return {
        'timeline': [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }