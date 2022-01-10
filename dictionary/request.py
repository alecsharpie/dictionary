import requests
import sys

sys.args()

def get_origin(word):
    response = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}').json()
    return response[0]['origin']


if __name__ == "__main__":
    print(get_origin())
