from utils import get_vessel_list, get_vessel_positions

def find_northernmost_vessel(year):
    vessel_ids = get_vessel_list()
    northernmost_vessel = None
    max_latitude = -90

    for vessel_id in vessel_ids:
        positions = get_vessel_positions(vessel_id, year)
        
        # Find the position with the highest latitude for this vessel
        if positions:
            northernmost_position = max(positions, key=lambda pos: pos['lat'])
            print(f"Vessel ID: {vessel_id}, Max Latitude: {northernmost_position['lat']}, Date: {northernmost_position['date']}")  # Debug print
            
            if northernmost_position['lat'] > max_latitude:
                max_latitude = northernmost_position['lat']
                northernmost_vessel = {
                    "vessel_id": vessel_id,
                    "latitude": northernmost_position['lat'],
                    "date": northernmost_position['date']
                }

    # Print the vessel that reached the farthest north
    print(f"\nThe northernmost vessel in {year} is {northernmost_vessel['vessel_id']} "
          f"at latitude {northernmost_vessel['latitude']} on {northernmost_vessel['date']}.")

