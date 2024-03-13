from weather_api_service import api_service


def convert(answer_from_api_service=api_service()):
    info = answer_from_api_service['info']
    url = info['url']
    fact = answer_from_api_service['fact']
    temp = fact['temp']
    feels = fact['feels_like']
    print()
    print(f'Температура по введенным тобою координатам: {temp}')
    print(f'Ощущается как: {feels}')
    print(f'Для более подробной информации предлагаю ссылочку от Яндекс-сервиса: {url}')


convert()
