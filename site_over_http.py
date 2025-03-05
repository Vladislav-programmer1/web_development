from bs4 import BeautifulSoup
import requests

html = requests.request(method="GET",
                        url="https://education.yandex.ru/",
                        ).content.decode("UTF-8")

search = r'<img[^>]+src="([^">]+)"'
soup = BeautifulSoup(html, "html.parser")
for post in soup.find_all("a", class_="post-card"):
    title = post.find(class_="post-card-title").text
    print(title)