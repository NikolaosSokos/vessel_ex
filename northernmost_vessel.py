import requests

def get_vessel_list():
    """Fetch the list of all vessels and print their IDs."""
    url = "https://localisation.flotteoceanographique.fr/api/v2/vessels"
    response = requests.get(url, verify=False)  
    response.raise_for_status() 
    vessels = response.json()  
    vessel_ids = [vessel['id'] for vessel in vessels]  
    
    print("Vessel IDs:", vessel_ids)
    return vessel_ids

get_vessel_list()
