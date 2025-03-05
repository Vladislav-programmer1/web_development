import requests
import sys
from json import dump

from PyQt6.QtWidgets import QWidget, QApplication, QLabel
from PyQt6.QtGui import QPixmap

SERVER_GEOCODE_ADDRESS = 'http://geocode-maps.yandex.ru/1.x/?'
SERVER_IMAGE_ADDRESS = 'https://static-maps.yandex.ru/v1?'
API_GEOCODE_KEY = '8013b162-6b42-4997-9691-77b7074026e0'
API_IMAGE_KEY = 'f3a0fe3a-b07e-4840-a1da-06f18b2ddf13'
SCREEN_SIZE = [600, 450]


def find_coordinates(geocode):
    geocoder_request = f'{SERVER_GEOCODE_ADDRESS}apikey={API_GEOCODE_KEY}&geocode={geocode}&format=json'
    response = requests.get(geocoder_request)
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]

    return toponym


class GeoMap(QWidget):
    def __init__(self, geo_objects: list[tuple[str, str]]):
        super().__init__()

        self.pixmap = None
        self.images = []
        self.get_images(geo_objects)
        self.number = 0
        self.initUI()

    def get_images(self, images_names):
        result = []
        for name, spn in images_names:
            coordinates = ",".join(find_coordinates(name).split())
            ll_spn = f"ll={coordinates}&spn={spn},{spn}"

            map_request = f"{SERVER_IMAGE_ADDRESS}{ll_spn}&apikey={API_IMAGE_KEY}"
            response = requests.get(map_request)

            if not response:
                print("Ошибка выполнения запроса:")
                print(map_request)
                print("Http статус:", response.status_code, "(", response.reason, ")")
                sys.exit(1)

            pixmap = QPixmap()
            pixmap.loadFromData(response.content)
            result.append(pixmap)
        self.images = result

    def initUI(self):
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(600, 450)
        pixmap = self.images[self.number]
        self.image.setPixmap(pixmap)

    def update(self):
        pixmap = self.images[self.number]
        self.image.setPixmap(pixmap)

    def keyPressEvent(self, a0):
        self.swipe_slide()

    def swipe_slide(self):
        self.number += 1
        self.number %= len(self.images)
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GeoMap([("Стамбул", "0.2"), ("гора Эльбрус", "0.2"), ("деревня Киберспасское", "0.03"),
                 ("Вена", "0.2"), ("деревня Хохотуй", "0.03"), ("деревня Мухоудёровка", "0.03")])
    ex.show()
    sys.exit(app.exec())