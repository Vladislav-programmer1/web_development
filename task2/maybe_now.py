import sys
import json
import requests

from io import BytesIO
from PIL import Image
from get_ll_spn import get_ll_spn


def get_toponym(toponym_to_find):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": "8013b162-6b42-4997-9691-77b7074026e0",
        "geocode": toponym_to_find,
        "format": "json"}

    toponym = requests.get(geocoder_api_server, params=geocoder_params).json()
    return toponym


def show_image(image_bytes):
    im = BytesIO(image_bytes)
    opened_image = Image.open(im)
    opened_image.show()


def get_image(ll, spn):
    apikey = "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13"
    map_api_server = "https://static-maps.yandex.ru/v1"
    print(ll)
    map_params = {"ll": ll, "spn": spn, "apikey": apikey, "pm": f"{ll},pmwtm1"}

    response = requests.get(map_api_server, params=map_params)
    return response.content


if __name__ == "__main__":
    toponym_ = get_toponym("Арена Омск")
    show_image(get_image(*get_ll_spn(toponym_)))