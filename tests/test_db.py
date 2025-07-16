import unittest
from peewee import *
import sqlite3

from app import TimelinePost
from playhouse.shortcuts import model_to_dict


# use an in-memory SQLite for tests.
test_db = SqliteDatabase(':memory:')
MODELS = [TimelinePost]


class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        # Bind model classes to test db. Since we have a complete list of
        # all models, we do not need to recursively bind dependencies.
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)

        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        # Not strictly necessary since SQLite in-memory databases only live
        # for the duration of the connection, and in the next step we close
        # the connection...but a good practice all the same.
        test_db.drop_tables(MODELS)

        # Close connection to db.
        test_db.close()

        # If we wanted, we could re-bind the models to their original
        # database here. But for tests this is probably not necessary.

    def test_timeline_post(self):
        # Create 2 timeline posts.
        first_post = TimelinePost.create(
            name="John Doe", email="john@example.com", content="Hello world, I'm John!"
        )
        assert first_post.id == 1
        second_post = TimelinePost.create(
            name="Jane Doe", email="jame@example.com", content="Hello world, I'm Jane"
        )
        assert second_post.id == 2
        # TODO: Get timeline posts and assert that they are correct
        # copy the logic of getPosts in app
        posts = [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]

        self.assertEqual(len(posts), 2)
        self.assertEqual(posts[0]["name"], "Jane Doe")
        self.assertEqual(posts[1]["email"], "john@example.com")
        self.assertEqual(posts[0]["content"], "Hello world, I'm Jane")
        self.assertEqual(posts[1]["content"], "Hello world, I'm John!")
        self.assertEqual(posts[0]["id"], 2)
        self.assertEqual(posts[1]["id"], 1)



