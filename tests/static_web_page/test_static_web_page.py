import pytest
from app import app

def test_accept_get_request():
    """
    Make a GET request to the main webpage, it should return
    a 200 response and have a Content-Type: header of 
    text/html; charset=utf-8
    """
    # Make HTTP response
    response = app.test_client().get("/")

    # Run assertions
    assert response.status_code == 200
    assert response.content_type == "text/html; charset=utf-8"

def test_reject_post_request():
    """
    Make a POST request to the main webpage, it should fail
    and return a 405 error and have a Content-Type: header of
    text/html; charset=utf-8
    """
    # Make HTTP response
    response = app.test_client().post("/")

    # Run assertions
    assert response.status_code != 200
    assert response.status_code == 405
    assert response.content_type == "text/html; charset=utf-8"
