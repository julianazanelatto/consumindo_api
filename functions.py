import requests


def get_weather_from_api(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&q={city_name}"
    response = requests.get(complete_url)
    return response.json()


def get_weather(city_name):
    api_key = "ef32bc4ad39070656ad8824b026af312"
    weather_data = get_weather_from_api(city_name, api_key)
    # retorna um dict
    print(weather_data)

    if weather_data["cod"] == 401:
        print('Problema durante a requisição!\n'
              f'Mensagem: {weather_data['message']}')

    elif weather_data["cod"] != '404':
        main_weather = weather_data["weather"][0]["main"]
        temperature = weather_data["main"]["temp"]
        print(f"Clima em {city_name}: {main_weather}")
        print(f"Temperatura: {temperature - 273.15:.2f}°C")

    else:
        print("Cidade não encontrada!")
