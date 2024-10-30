import requests
from datetime import datetime
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
BASE_URL = "https://localisation.flotteoceanographique.fr/api/v2"

def get_vessel_list():
    url = f"{BASE_URL}/vessels"
    response = requests.get(url, verify=False)
    response.raise_for_status()
    vessels = response.json()
    return [vessel['id'] for vessel in vessels]

def year_to_iso8601(year):
    start_of_year = datetime(year, 1, 1).strftime("%Y-%m-%dT00:00:00.000Z")
    end_of_year = datetime(year, 12, 31, 23, 59, 59).strftime("%Y-%m-%dT23:59:59.000Z")
    return start_of_year, end_of_year

def get_vessel_positions(vessel_id, year):
    url = f"{BASE_URL}/vessels/{vessel_id}/positions"
    start_date, end_date = year_to_iso8601(year)
    params = {'startDate': start_date, 'endDate': end_date}
    response = requests.get(url, params=params, verify=False)
    response.raise_for_status()
    return response.json()
