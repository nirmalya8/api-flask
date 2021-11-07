import pytest
import requests
from requests import status_codes

url = 'http://127.0.0.1:5000/'

def test_home_page():
    resp = requests.get(url)
    assert resp.status_code == 200


def test_order_taking():
    for i in range(7):
        resp  = requests.get(url+'order/'+str(i))
        if i<=5:
            assert resp.status_code == 200
        else :
            assert resp.status_code == 404

def test_showing_orders():
    resp = requests.get(url+'show')
    response = resp.json()
    if type(response['Your orders']) == str:
        assert resp.status_code == 404
    else:
        assert resp.status_code == 200

def test_deleting_orders():
    for i in range(7):
        resp = requests.get(url+'delete/'+str(i))
        response = resp.json()
        if response['Status'] =='Wasn\'t in the menu':
            assert resp.status_code == 404
        else:
            assert resp.status_code == 200

