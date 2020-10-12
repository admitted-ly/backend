import requests
import json


def get_colleges_list(sat_score, zip_code):
    request_url = "https://us-central1-admittedly.cloudfunctions.net/Query"
    payload = {'SAT': sat_score, 'zipcode': str(zip_code)}
    response = ''

    try:
        response = requests.get(request_url, params=payload)
        return response.json()

    except json.decoder.JSONDecodeError:
        response = 'resource returned is not in json format'
    