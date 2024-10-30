from utils import get_vessel_list, get_vessel_positions

def find_max_average_temp_vessel(year):
    """Finds the vessel with the highest average temperature in the specified year."""
    vessel_ids = get_vessel_list()
    vessels_avg_temps = []

    for vessel_id in vessel_ids:
        positions = get_vessel_positions(vessel_id, year)
        
        # Collect combined average temperatures for each position
        temperature_sums = []
        
        for pos in positions:
            data = pos.get('data', {})
            seatemp = data.get('seatemp')
            airtemp = data.get('airtemp')
            
            # Only calculate if both seatemp and airtemp are available
            if seatemp is not None and airtemp is not None:
                combined_temp = (seatemp + airtemp) / 2
                temperature_sums.append(combined_temp)
        
        # Calculate and print the average temperature for this vessel
        if temperature_sums:
            avg_temp = sum(temperature_sums) / len(temperature_sums)
            print(f"Vessel ID: {vessel_id}, Average Temperature: {avg_temp:.2f}°C.")  # Debug print
            vessels_avg_temps.append({
                "vessel_id": vessel_id,
                "average_temperature": avg_temp
            })

    # Use max() to find the vessel with the highest average temperature
    if vessels_avg_temps:
        vessel_with_max_avg_temp = max(vessels_avg_temps, key=lambda v: v['average_temperature'])
        print(f"\nThe vessel with the highest average temperature in {year} is "
          f"{vessel_with_max_avg_temp['vessel_id']} with an average temperature of "
          f"{vessel_with_max_avg_temp['average_temperature']:.2f}°C.")
    else:
        print(f"No temperature data available for any vessels in {year}.")

