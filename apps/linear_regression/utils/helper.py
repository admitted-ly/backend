import requests


def get_colleges_list(sat_score, zip_code):

    request_url = "https://us-central1-admittedly.cloudfunctions.net/Query"
    payload = {'SAT': sat_score, 'zipcode': 'zip_code'}

    response = requests.get(request_url, params=payload)

    return response.json()