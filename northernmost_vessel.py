import requests
from datetime import datetime
def get_vessel_list():
    """Fetch the list of all vessels and print their IDs."""
    url = "https://localisation.flotteoceanographique.fr/api/v2/vessels"
    response = requests.get(url, verify=False)  
    response.raise_for_status() 
    vessels = response.json()  
    vessel_ids = [vessel['id'] for vessel in vessels]  
    
    print("Vessel IDs:", vessel_ids)
    return vessel_ids

def get_vessel_positions(vessel_id, start_date="2021-01-01", end_date="2021-12-31"):
    url = f"https://localisation.flotteoceanographique.fr/api/v2/vessels/{vessel_id}/positions"
    params = {'startDate': start_date, 'endDate': end_date}

    response = requests.get(url, params=params, verify=False)
    response.raise_for_status()
    return response.json()

def find_northernmost_vessel():
    vessel_ids = get_vessel_list()
    northernmost_vessel = None
    max_latitude = -90  # Start with the lowest possible latitude

    for vessel_id in vessel_ids:
        positions = get_vessel_positions(vessel_id)
        
        for position in positions:
            latitude = position['lat']
            date = position['date']
            if latitude > max_latitude:
                max_latitude = latitude
                northernmost_vessel = {
                    "vessel_id": vessel_id,
                    "latitude": latitude,
                    "date": date
                }
    
    print(f"The northernmost vessel in 2021 is {northernmost_vessel['vessel_id']} "
          f"at latitude {northernmost_vessel['latitude']} on {northernmost_vessel['date']}.")

find_northernmost_vessel()
