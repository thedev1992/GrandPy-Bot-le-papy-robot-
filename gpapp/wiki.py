#! /usr/bin/env python3
# coding: utf-8

import wikipedia
from wikipedia import exceptions


class Wiki:

    # Get the question as an attribute
    def __init__(self, place):
        wikipedia.set_lang("fr")
        self.place = " " + place

    # Return the first 2 sentence of wiki
    def wiki_quote(self):
        try:
            search = wikipedia.search(self.place)
            print(search)
            if search:
                title_page = search[0]
                text = wikipedia.summary(title_page, sentences=2)
                name_page = title_page.replace(" ", "_")
                link = "https://fr.wikipedia.org/wiki/" + name_page
                result = ("Hum ... Hum ... Eureka : " + text + " Le lien de la page complete " + link)

            else:
                result = ("Je t'affiche ce qui me parait le plus proche "
                          "mais nous savons que ce n'est pas ce que tu cherchais. "
                          "Ou alors je t'affiche ma ville de naissance... Hum ..."

                          )
            return result
        except exceptions.DisambiguationError:
            result = "J'ai un problème, j'ai trop de réponses pour toi du coup j'en ai aucune !"
            return result
