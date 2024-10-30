from utils import get_vessel_list,get_vessel_positions
def find_northernmost_vessel(year):
    vessel_ids = get_vessel_list()
    northernmost_vessel = None
    max_latitude = -90  # Initialize the lowest possible latitude
    
    # Loop for finding northernmost point
    for vessel_id in vessel_ids:
        positions = get_vessel_positions(vessel_id, year)
        
        # Use max() for faster results
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