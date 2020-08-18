import pytest
import requests
import urllib.request

from gpapp.map import GoogleMap


# no entry
def test_no_entry(monkeypatch):
    result = "1"
    gmap = GoogleMap("")

    monkeypatch.setattr(urllib.request, 'urlopen', result)

    assert gmap.get_gps_coord() == result


# Stade de France
def test_get_coord(monkeypatch):
    result = {'lat': 48.9244592, 'lng': 2.3601645}
    gmap = GoogleMap("Stade de france")

    monkeypatch.setattr(urllib.request, 'urlopen', result)

    assert gmap.get_gps_coord() == result


# address eiffel tower
def test_get_address(monkeypatch):
    result = " Champ de Mars 5 Avenue Anatole France Paris 75007"
    gmap = GoogleMap("Tour eiffel")

    monkeypatch.setattr(urllib.request, 'urlopen', result)

    assert gmap.get_adress() == result
