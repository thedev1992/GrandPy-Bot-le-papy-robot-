#! /usr/bin/env python3
# coding: utf-8

import requests


class GoogleMap:

    def __init__(self, question):
        self.url = "https://maps.googleapis.com/maps/api/geocode/json?address="
        self.key = "AIzaSyDMgIhs_f-La3QBapEwe-dy80PHDxU9alk"
        self.question = '+'.join(question.split())

    # return the lat and the lng of the attribute question
    def get_gps_coord(self):
        response = requests.get(self.url + self.question + "&key=" + self.key)
        resp_json = response.json()
        try:
            return resp_json['results'][0]['geometry']['location']
        except IndexError:
            return "1"

    # return the address of the attribute question
    def get_adress(self):
        response = requests.get(self.url + self.question + "&key=" + self.key)
        resp_json = response.json()
        try:
            address = ""
            for i in range(4):
                address = address +\
                          " " + \
                          resp_json["results"][0]["address_components"][i]["long_name"]
            address = address + \
                      " " + \
                      resp_json["results"][0]["address_components"][-1]["long_name"]
            return address
        except IndexError:
            return "1"
