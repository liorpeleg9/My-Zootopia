import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = "https://api.api-ninjas.com/v1/animals"


def fetch_data(animal_name: str):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals (list of dictionaries).
    Each animal dict typically includes:
      'name', 'taxonomy', 'locations', 'characteristics'
    """
    if not API_KEY:
        raise RuntimeError("Missing API_KEY. Add it to your .env file (API_KEY=...).")

    animal_name = animal_name.strip()
    if not animal_name:
        return []

    headers = {"X-Api-Key": API_KEY}
    params = {"name": animal_name}

    response = requests.get(API_URL, headers=headers, params=params, timeout=20)

    if response.status_code != 200:
        raise RuntimeError(f"API error {response.status_code}: {response.text}")

    data = response.json()

    if isinstance(data, list):
        return data

    return []
