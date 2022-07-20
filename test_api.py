import requests
import pytest

from configuration import request_1, request_2, request_3


def test_request():
    print(request_1.json(), request_1.status_code)


def test_request_2():
    print(request_2.json(), request_2.status_code)


def test_request_3():
    print(request_3.json(), request_3.status_code)
