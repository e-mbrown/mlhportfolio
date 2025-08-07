import unittest
import os

os.environ["TESTING"] = "true"

from app import app


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>Portfolio</title>" in html
        # TODO Add more tests relating to the home page
        # check metadata
        assert '<meta charset="utf-8">' in html
        assert '<meta name="viewport"' in html
        assert '<meta property="og:title" content="Personal Portfolio">' in html
        
        # Change test because tailwind
        # assert '<img src="./static/img/logo.svg" />' in html
        assert "./static/dist/tailwind.css" in html

    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline" in json
        assert len(json["timeline"]) == 0
        # TODO Add more tests relating to the /api/timeline_post GET and POST apis
        post_request = self.client.post(
            "/api/timeline_post",
            data={
                "name": "John Doe",
                "email": "john@example.com",
                "content": "Hello world, I'm John!",
            },
        )
        assert post_request.status_code == 200

        post_json = post_request.get_json()
        assert post_json["name"] == "John Doe"
        assert post_json["email"] == "john@example.com"
        assert post_json["content"] == "Hello world, I'm John!"
        assert post_json["id"] == 1

        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        data = response.get_json()
        assert "timeline" in data
        assert len(data["timeline"]) == 1

        assert data["timeline"][0]["id"] == 1
        assert data["timeline"][0]["name"] == "John Doe"
        assert data["timeline"][0]["email"] == "john@example.com"
        assert data["timeline"][0]["content"] == "Hello world, I'm John!"

        # TODO Add more tests relating to the timeline page
        page_response = self.client.get("/timeline")
        assert page_response.status_code == 200
        html = page_response.get_data(as_text=True)
        assert "<title>Timeline</title>" in html
        assert '<meta charset="UTF-8">' in html
        assert "John Doe" in html
        assert "Hello world, I&#39;m John!" in html
        assert "john@example.com" in html

        # add second test
        second_post_request= self.client.post(
            "/api/timeline_post",
            data={
                "name": "Jane Doe",
                "email": "jane@example.com",
                "content": "Hi, I’m Jane!",
            },
        )
        second_post_request = self.client.get("/api/timeline_post")
        data = second_post_request.get_json()
        assert len(data["timeline"]) == 2
        assert data["timeline"][0]["name"] == "Jane Doe"  # Newest first
        assert data["timeline"][1]["name"] == "John Doe"
        assert data["timeline"][0]["content"] == "Hi, I’m Jane!"
        assert data["timeline"][0]["id"] == 2

    def test_malformed_timeline_post(self):
        # POST request missing name
        response = self.client.post(
            "/api/timeline_post",
            data={"email": "john@example.com", "content": "Hello world, I'm John!"},
        )
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html

        # POST request with empty content
        response = self.client.post(
            "/api/timeline_post",
            data={"name": "John Doe", "email": "john@example.com", "content": ""},
        )
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        # POST request with malformed email
        response = self.client.post(
            "/api/timeline_post",
            data={
                "name": "John Doe",
                "email": "not-an-email",
                "content": "Hello world, I'm John!",
            },
        )
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html
