import requests


SERVER_GEOCODE_ADDRESS = 'http://geocode-maps.yandex.ru/1.x/?'
API_GEOCODE_KEY = '8013b162-6b42-4997-9691-77b7074026e0'


def get_latitude(geocode):
    geocoder_request = f'{SERVER_GEOCODE_ADDRESS}apikey={API_GEOCODE_KEY}&geocode={geocode}&format=json'
    response = requests.get(geocoder_request)
    json_response = response.json()
    latitude = json_response["response"]["GeoObjectCollection"]["featureMember"][0][
        "GeoObject"]["Point"]["pos"].split()[1]

    return latitude


cities = input().split(",")
result = min(list(map(lambda x: (get_latitude(x), x), cities)), key=lambda x: x[0])[1]
print(result)