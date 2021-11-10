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


def test_show_price():
    resp = requests.get(url+'price')
    response = resp.json()
    if(response['Price']==0):
        assert resp.status_code == 404
    else:
        assert resp.status_code == 200

def test_show_menucard():
    resp = requests.get(url+'showmenu')
    assert resp.status_code == 200

def test_adding_to_menucard():
    resp = requests.get(url+'showmenu')
    response = resp.json()
    resp1 = requests.get(url+'additem')
    resp2 = requests.get(url+'showmenu')
    response2 = resp2.json()
    if len(response2['Menu']) > len(response['Menu']):
        assert resp1.status_code == 201
    else: 
        assert resp.status_code == 400

def test_deleting_from_menucard():
    resp = requests.get(url+'showmenu')
    response = resp.json()
    resp1 = requests.get(url+'delitem')
    resp2 = requests.get(url+'showmenu')
    response2 = resp2.json()
    if len(response2['Menu']) < len(response['Menu']):
        assert resp1.status_code == 200
    else:
        assert resp.status_code == 404