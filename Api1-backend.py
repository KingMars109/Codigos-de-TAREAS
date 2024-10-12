import requests

from googletrans import Translator


url = 'https://catfact.ninja/fact'

response = requests.get(url)

if response.status_code == 200:

    data = response.json()
    fact = data['fact']

    translator = Translator()
    translation = translator.translate(fact, src='en', dest='es')

    print("Dato sobre gatos :", translation.text)
else:
    print("Error al realizar la solicitud:", response.status_code)