import pytest

from utils import get_data, get_last_data, get_formatted_data, get_filtered_data


def test_get_data():
    url = "https://api.npoint.io/965a8959441d23a36a83"
    assert get_data(url) is not None
    url = "https://api.npoint.io/965a8959441d23a36a84"
    data, info = get_data(url)
    assert data is None
    assert info == "WARNING: Cтатус ответа 500"
    url = "https://api.point.io/965a8959441d23a36a84"
    data, info = get_data(url)
    assert data is None
    assert info == "ERROR: requests.exceptions.ConnectionError"


def test_get_filtered_data(test_data):
    assert len(get_filtered_data(test_data)) == 4
    assert len(get_filtered_data(test_data, filtered_empty_from=2)) == 2



def test_get_last_data(test_data):
    data = get_last_data(test_data, count_last_values=2)
    assert data[0]["date"] == '2019-08-26T10:50:58.294041'
    assert len(data) == 2


def test_get_formatted_data(test_data):
    data = get_formatted_data(test_data[:1])
    assert data == ['26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб.\n']
    data = get_formatted_data(test_data[1:2])
    assert data == ['03.07.2019 Перевод организации\n[СКРЫТО]  -> Счет **5560\n8221.37 USD\n']