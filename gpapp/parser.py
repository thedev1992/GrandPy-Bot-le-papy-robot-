#! /usr/bin/env python3
# coding: utf-8

import json
import re


class Parser:

    # Open the word's file
    def __init__(self, ):
        with open('word.json', encoding='utf-8' ) as json_data:
            data_dict = json.load(json_data)
            self.word = data_dict

    # Parse the string in parameters
    def sentence_parser(self, sentence):
        
        sentence = re.sub(r'[^\w\s]', ' ', sentence)
        sentence = sentence.lower()
        tab = sentence.split()
        i = 0
        while i < len(tab):
            if tab[i] in self.word:
                tab[i] = ""
            i += 1
        sentence = " ".join(tab)
        sentence = re.sub(' +', ' ', sentence)
        sentence = sentence.strip()
        return sentence
