import pytest

import requests


def test_case_add():
    """
    测试内容
    :return:
    """
    response = requests.post('http://127.0.0.1:8888/case/add', {'code': 'test3', 'content': 'test3 content'})
    assert response is not None, 'response is None'

    origin_data2 = response.json()
    assert origin_data2['feedback'] == 1

    response = requests.post('http://127.0.0.1:8888/case/add', {'code': 'Test1', 'content': 'test1 content'})
    origin_data2 = response.json()
    assert origin_data2['feedback'] == -1
