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
    def __init__(self, geo_object: str, spn: str):
        super().__init__()

        self.pixmap = None
        self.get_image(geo_object, spn)
        self.initUI()

    def get_image(self, name, spn):
        coordinates = ",".join(find_coordinates(name).split())
        ll_spn = f"ll={coordinates}&spn={spn},{spn}"

        map_request = f"{SERVER_IMAGE_ADDRESS}{ll_spn}&apikey={API_IMAGE_KEY}"
        response = requests.get(map_request)

        if not response:
            print("Ошибка выполнения запроса:")
            print(map_request)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)

        self.map_file = "map.png"
        with open(self.map_file, "wb") as file:
            file.write(response.content)

    def initUI(self):
        self.setGeometry(100, 100, *SCREEN_SIZE)
        self.setWindowTitle('Отображение карты')

        self.pixmap = QPixmap(self.map_file)
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(600, 450)
        self.image.setPixmap(self.pixmap)

    def closeEvent(self, event):
        """При закрытии формы подчищаем за собой"""
        os.remove(self.map_file)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GeoMap("Австралия", "20")
    ex.show()
    sys.exit(app.exec())