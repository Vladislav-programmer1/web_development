def get_ll_spn(toponym: dict) -> tuple:
    longitude, latitude = toponym["response"]["GeoObjectCollection"]["featureMember"][0][
        "GeoObject"]["Point"]["pos"].split()

    ll = ",".join([longitude, latitude])

    envelope = toponym["response"]["GeoObjectCollection"]["featureMember"][0][
        "GeoObject"]["boundedBy"]["Envelope"]

    l, b = envelope["lowerCorner"].split(" ")
    r, t = envelope["upperCorner"].split(" ")

    dx = abs(float(l) - float(r)) / 2
    dy = abs(float(b) - float(t)) / 2

    spn = f"{dx},{dy}"

    return ll, spn