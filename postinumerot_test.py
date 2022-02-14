# Kirjoita postinumerot-moduulin testit tähän tiedostoon
from urllib.request import urlopen
import json
import pytest

url = "https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json"

response = urlopen(url)

data_json = json.loads(response.read())



#pst = input("Kirjoita postitoimipaikka: ")

#pst = pst.upper()

def postinumerot(paikka):
    pst = paikka
    output = ''
    pst = pst.upper()
    if pst not in data_json.values():
        print('Tuntematon postitoimipaikka')
    else:
        output = [key for key,value in data_json.items() if value == str(pst)]

        output.sort()

    return output

def test_postinumerot1():
    for x in data_json.values():
        assert x

