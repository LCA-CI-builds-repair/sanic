import inspect
import pytest

from sanic.helpers import has_message_body
from sanic.config import Config


def test_has_message_body():
    # Test cases for checking if a message body is expected based on the status code
    tests = (
        (100, False),  # Continue response should not have a message body
        (102, False),  # Processing response should not have a message body
        (204, False),  # No Content response should not have a message body
        (200, True),   # OK response should have a message body
        (304, False),  # Not Modified response should not have a message body
        (400, True),   # Bad Request response should have a message body
    )
    for status_code, expected in tests:
        assert has_message_body(status_code) is expected
def test_is_entity_header():
def test_is_entity_header():
    # Test cases for checking if a header is an entity header
    tests = (
        ("allow", True),
        ("extension-header", True),
        ("", False),
        ("test", False),
    )
    for header, expected in tests:
        assert helpers.is_entity_header(header) is expected


def test_is_hop_by_hop_header():
    # Test cases for checking if a header is a hop-by-hop header
    tests = (
        ("connection", True),
        ("upgrade", True),
        ("", False),
        ("test", False),
    )
    for header, expected in tests:
        assert helpers.is_hop_by_hop_header(header) is expected
def test_remove_entity_headers():
    tests = (
        ({}, {}),
        ({"Allow": "GET, POST, HEAD"}, {}),
        (
            {
                "Content-Type": "application/json",
                "Expires": "Wed, 21 Oct 2015 07:28:00 GMT",
                "Foo": "Bar",
            },
            {"Expires": "Wed, 21 Oct 2015 07:28:00 GMT", "Foo": "Bar"},
        ),
        (
            {"Allow": "GET, POST, HEAD", "Content-Location": "/test"},
            {"Content-Location": "/test"},
        ),
    )

    for header, expected in tests:
        assert helpers.remove_entity_headers(header) == expected


def test_import_string_class():
    obj = helpers.import_string("sanic.config.Config")
    assert isinstance(obj, Config)


def test_import_string_module():
    module = helpers.import_string("sanic.config")
    assert inspect.ismodule(module)


def test_import_string_exception():
    with pytest.raises(ImportError):
        helpers.import_string("test.test.test")
