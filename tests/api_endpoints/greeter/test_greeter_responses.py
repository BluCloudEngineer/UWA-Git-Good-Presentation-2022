import pytest
from app import app

def test_accept_get_request():
    """
    Make a HTTP GET request to the main webpage, it should
    return a 200 response and have a Content-Type header of
    text/html; charset=utf-8
    """
    # Make HTTP response
    response = app.test_client().get("/greeter")

    # Run assertions
    assert response.status_code == 200
    assert response.content_type == "text/html; charset=utf-8"

def test_reject_post_request():
    """
    Make a HTTP POST request to the main webpage, it should
    fail and return a 405 error and have a Content-Type
    header of text/html; charset=utf-8
    """
    # Make HTTP response
    response = app.test_client().post("/greeter")

    # Run assertions
    assert response.status_code != 200
    assert response.status_code == 405
    assert response.content_type == "text/html; charset=utf-8"


def test_anonymous_user_1():
    """
    Make a HTTP GET request to the greeter API endpoint but
    do not include any parameters
    """
    # Make HTTP response
    response = app.test_client().get("/greeter")

    # Run assertions
    assert response.status_code == 200
    assert response.content_type == "text/html; charset=utf-8"
    assert response.data.decode("utf-8") == "Hi anonymous, what is your name?"

def test_anonymous_user_2():
    """
    Make a HTTP GET request to the greeter API endpoint with
    parameters but do not include "name"
    """
    # Make HTTP response
    response = app.test_client().get("/greeter", query_string={
        "food": "good",
        "caffeine": "low"
    })
    
    # Run assertions
    assert response.status_code == 200
    assert response.content_type == "text/html; charset=utf-8"
    assert response.data.decode("utf-8") == "Hi anonymous, what is your name?"
