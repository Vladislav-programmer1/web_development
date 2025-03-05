import os
import sys

import pygame
import requests


SERVER_GEOCODE_ADDRESS = 'http://geocode-maps.yandex.ru/1.x/?'
API_GEOCODE_KEY = '8013b162-6b42-4997-9691-77b7074026e0'


def find_coordinates(geocode):
    geocoder_request = f'{SERVER_GEOCODE_ADDRESS}apikey={API_GEOCODE_KEY}&geocode={geocode}&format=json'
    response = requests.get(geocoder_request)
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]

    return toponym


server_address = 'https://static-maps.yandex.ru/v1?'
api_key = 'f3a0fe3a-b07e-4840-a1da-06f18b2ddf13'
full_coordinates = ",".join(find_coordinates("Москва").split())
coordinates_1 = "37.554535,55.715763"
coordinates_2 = "37.560070,55.791672"
coordinates_3 = "37.440408,55.817840"
spn = "0.2"
ll_spn = f'll={full_coordinates}&spn={spn},{spn}'

map_request = (f"{server_address}{ll_spn}&lang=ru_RU&pt={coordinates_1},pmwtm1~{coordinates_2},pmblm2~"
               f"{coordinates_3},pmrdm3&apikey={api_key}")
print(map_request)
response = requests.get(map_request)

if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)

map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)

pygame.init()
screen = pygame.display.set_mode((600, 450))
screen.blit(pygame.image.load(map_file), (0, 0))
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()

os.remove(map_file)