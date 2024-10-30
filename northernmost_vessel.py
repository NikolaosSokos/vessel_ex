import requests
from datetime import datetime
import argparse
BASE_URL = "https://localisation.flotteoceanographique.fr/api/v2"

def get_vessel_list():
    url = f"{BASE_URL}/vessels"
    response = requests.get(url, verify=False)  
    response.raise_for_status() 
    vessels = response.json()  
    vessel_ids = [vessel['id'] for vessel in vessels]  
    return vessel_ids

def year_to_iso8601(year):
    start_of_year = datetime(year, 1, 1).strftime("%Y-%m-%dT00:00:00.000Z")  # Start of the year in UTC
    end_of_year = datetime(year, 12, 31, 23, 59, 59).strftime("%Y-%m-%dT23:59:59.000Z")  # End of the year in UTC
    return start_of_year, end_of_year

def get_vessel_positions(vessel_id, year):
    url = f"{BASE_URL}/vessels/{vessel_id}/positions"
    start_date, end_date = year_to_iso8601(year)  # Convert year to ISO 8601 start and end dates
    params = {'startDate': start_date, 'endDate': end_date}
    response = requests.get(url, params=params, verify=False)
    response.raise_for_status()
    return response.json()

def find_northernmost_vessel(year):
    vessel_ids = get_vessel_list()
    northernmost_vessel = None
    max_latitude = -90  # Initialize the lowest possible latitude
    
    # Loop through each vessel's positions and track the northernmost point
    for vessel_id in vessel_ids:
        positions = get_vessel_positions(vessel_id, year)
        
        # Use max() to find the position with the highest latitude, if any positions exist
        if positions:
            northernmost_position = max(positions, key=lambda pos: pos['lat'])
            if northernmost_position['lat'] > max_latitude:
                max_latitude = northernmost_position['lat']
                northernmost_vessel = {
                    "vessel_id": vessel_id,
                    "latitude": northernmost_position['lat'],
                    "date": northernmost_position['date']
                }
    
    print(f"The northernmost vessel in {year} is {northernmost_vessel['vessel_id']} "
          f"at latitude {northernmost_vessel['latitude']} at {northernmost_vessel['date']}.")

def main():
    parser = argparse.ArgumentParser(description="Find the northernmost vessel for a given year.")
    parser.add_argument("--year", type=int, default=2021, help="Specify the year to search (default is 2021)")
    args = parser.parse_args()
    
    find_northernmost_vessel(args.year)

# Run the script
if __name__ == "__main__":
    main()