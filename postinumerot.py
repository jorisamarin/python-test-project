# Kopioi aikaisempi ratkaisusi tänne. Lisää tarvittaessa myös muut ratkaisusi tiedostot.
from urllib.request import urlopen
import json
import pytest

url = "https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json"

response = urlopen(url)

data_json = json.loads(response.read())

pst = input("Kirjoita postitoimipaikka: ")

pst = pst.upper()

if pst not in dict.values(data_json):
    print('Tuntematon postitoimipaikka')
else:
    output = [key for key,value in data_json.items() if value == str(pst)]

    output.sort()

    print(*output, sep=", ")