import requests

BASE_URL = "https://freedictionaryapi.com/api/v1/entries/en/"

def retrieve_word(word):
    try:
        completed_url = BASE_URL + word
        response = requests.get( completed_url, headers={"Content-Type": "application/json"} )
        print(response.text)
        data = response.json()
        if len(data["entries"]):
            return data["entries"][0]
        else:
            return None
    except:
        return None