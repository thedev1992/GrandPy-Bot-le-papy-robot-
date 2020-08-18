# coding: utf-8

import wikipedia
import pytest
import urllib.request

from gpapp.wiki import Wiki


def test_no_entry(monkeypatch):
    result = "Je t'affiche ce qui me parait le plus proche mais nous savons que ce n'est pas ce que tu cherchais. " \
             "Ou alors je t'affiche ma ville de naissance... Hum ..."

    wiki = Wiki("")

    monkeypatch.setattr(urllib.request, 'urlopen', result)

    assert wiki.wiki_quote() == result


def test_quote(monkeypatch):
    result = "Hum ... Hum ... Eureka : La tour Eiffel  est une tour de fer puddlé de 324 mètres de hauteur " \
             "(avec antennes) située à Paris, à l’extrémité nord-ouest du parc du Champ-de-Mars en bordure " \
             "de la Seine dans le 7e arrondissement. Son adresse officielle est 5, avenue Anatole-France." \
             " Le lien de la page complete https://fr.wikipedia.org/wiki/Tour Eiffel"
    wiki = Wiki("tour eiffel")

    monkeypatch.setattr(urllib.request, 'urlopen', result)

    assert wiki.wiki_quote() == result
