from flask import Flask, url_for

app = Flask(__name__)
STANDARD_REQUEST = """<!DOCTYPE html>
                        <html lang="en">
                        <head>
                            <meta charset="UTF-8">
                            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
                            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
                            <title>Document</title>
                        </head>
                        <body>
                            <h1>{}</h1>
                            <h2>{}</h2>
                            <div class="alert alert-primary" role="alert">
                                {}
                              </div>
                              <div class="alert alert-secondary" role="alert">
                                {}
                              </div>
                              <div class="alert alert-success" role="alert">
                                {}
                              </div>
                              <div class="alert alert-danger" role="alert">
                                {}
                        </body>
                        </html>"""


@app.route("/choice/mars")
def mars():
    reasons = [
        "Мое предложение: Марс",
        "Эта планета близка к земле",
        "На ней есть атмосфера и вода",
        "На ней много необходимых ресурсов",
        "На ней есть небольшое магнитное поле",
        "Наконец, она просто красива"
    ]

    return STANDARD_REQUEST.format(*reasons)


@app.route("/choice/earth")
def earth():
    reasons = [
        "Консервативный взгляд: Земля",
        "Земля - наш родной дом",
        "Здесь всё кажется родным",
        "Здесь достаточно ресурсов",
        "Здесь есть превосходный климат",
        "Наконец, земля невероятно красива!"
    ]

    return STANDARD_REQUEST.format(*reasons)


@app.route("/choice/venera")
def venera():
    reasons = [
        "Мое предложение: Венера",
        "Эта  планета близка к земле",
        "На ней есть атмосфера",
        "Она близка к солнцу и может быть колонизирована",
        "На най очень много важных ресурсов",
        "Её вид из космоса великолепен"
    ]

    return STANDARD_REQUEST.format(*reasons)


@app.route("/")
def main():
    motivation_words = [
        "Единственное спасение для человечества",
        "Только так мы обретём истинную власть"
    ]
    return """<!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <title>Document</title>
                </head>
                <body>
                    <h1>{}</h1>
                    <h2>{}</h2>
                </body>
                </html>""".format(*motivation_words)


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")