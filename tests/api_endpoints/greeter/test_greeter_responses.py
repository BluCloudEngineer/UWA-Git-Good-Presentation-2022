"""
Python Flask web application Unit Tests
"""
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


def test_gordon_freeman_request():
    """
    Make a HTTP GET request to the greeter API endpoint with
    the name parameter set to Gordon Freeman
    """
    # Make HTTP response
    response = app.test_client().get("/greeter", query_string={
        "name": "Gordon Freeman"
    })

    # Run assertions
    assert response.status_code == 200
    assert response.content_type == "text/html; charset=utf-8"
    assert response.data.decode("utf-8") == "Wake up Mr Freeman!"


def test_adam_jensen_request():
    """
    Make a HTTP GET request to the greeter API endpoint with
    the name parameter set to Adam Jensen
    """
    # Make HTTP response
    response = app.test_client().get("/greeter", query_string={
        "name": "Adam Jensen"
    })

    # Run assertions
    assert response.status_code == 200
    assert response.content_type == "text/html; charset=utf-8"
    assert response.data.decode("utf-8") == "I never asked for this..."


def test_obi_wan_kenobi_request():
    """
    Make a HTTP GET request to the greeter API endpoint with
    the name parameter set to the following:
    1.  Obi Wan
    2.  Obi-Wan
    3.  Obi-Wan Kenobi
    """
    names = [
        "Obi Wan",
        "Obi-Wan",
        "Obi-Wan Kenobi"
    ]
    for name in names:
        # Make HTTP response
        response = app.test_client().get("/greeter", query_string={
            "name": name
        })

        # Run assertions
        assert response.status_code == 200
        assert response.content_type == "text/html; charset=utf-8"
        assert response.data.decode("utf-8") == "Hello There!"


def test_tf2_heavy_request():
    """
    Make a HTTP GET request to the greeter API endpoint with
    the name parameter set to Heavy
    """
    # Make HTTP response
    response = app.test_client().get("/greeter", query_string={
        "name": "Heavy"
    })

    # Run assertions
    assert response.status_code == 200
    assert response.content_type == "text/html; charset=utf-8"
    assert response.data.decode(
        "utf-8") == "It costs four hundred thousand dollars to fire this weapon, for twelve seconds."


def test_default_request():
    """
    Make a HTTP GET request to the greeter API endpoint with
    the name parameter set to the following:
    1.  Bob
    2.  Jessica
    3.  Rex
    4.  Dilbert
    """
    tests = [
        ["Bob", "Hi Bob!"],
        ["Jessica", "Hi Jessica!"],
        ["Rex", "Hi Rex!"],
        ["Dilbert", "Hi Dilbert!"]
    ]
    for test in tests:
        # Make HTTP response
        response = app.test_client().get("/greeter", query_string={
            "name": test[0]
        })

        # Run assertions
        assert response.status_code == 200
        assert response.content_type == "text/html; charset=utf-8"
        assert response.data.decode("utf-8") == test[1]


def test_readme_example():
    """
    Make a HTTP GET request to the greeter API endpoint with
    the name parameter set to test, just like in the
    README.md file
    """
    # Make HTTP response
    response = app.test_client().get("/greeter", query_string={
        "name": "test"
    })

    # Run assertions
    assert response.status_code == 200
    assert response.content_type == "text/html; charset=utf-8"
    assert response.data.decode("utf-8") == "Hi Test!"
