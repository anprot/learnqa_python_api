from json.decoder import JSONDecodeError
import requests


response = requests.get('https://gist.github.com/KotovVitaliy/83e4eeabdd556431374dfc70d0ba9d37')
print(response.text)

try:
    json_text = response.json()
    print(json_text)
except JSONDecodeError:
    print("Response is not as JSON format")