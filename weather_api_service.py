import requests
from title_and_coordinates import title_coords


def api_service(coords=title_coords()):
    lat, long = coords.split(", ")
    params = {'lat': lat,
              'lon': long,
              'lang': 'ru_RU'}
    api_key = 'fa321d85-0558-46ca-91a8-4357f6e82842'
    url = 'https://api.weather.yandex.ru/v2/informers'
    headers = {'X-Yandex-API-Key': api_key}
    return requests.get(url, params=params, headers=headers).json()
