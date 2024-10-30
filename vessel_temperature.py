from utils import get_vessel_list, get_vessel_positions

def find_max_average_temp_vessel(year):
    vessel_ids = get_vessel_list()
    max_avg_temp = float('-inf')
    vessel_with_max_avg_temp = None

    for vessel_id in vessel_ids:
        positions = get_vessel_positions(vessel_id, year)
        
        # Calculate average temperature if temperature data exists
        temperatures = [pos['temperature'] for pos in positions if 'temperature' in pos]
        if temperatures:
            avg_temp = sum(temperatures) / len(temperatures)
            if avg_temp > max_avg_temp:
                max_avg_temp = avg_temp
                vessel_with_max_avg_temp = {
                    "vessel_id": vessel_id,
                    "average_temperature": avg_temp
                }

    print(f"The vessel with the highest average temperature in {year} is {vessel_with_max_avg_temp['vessel_id']} "
          f"with an average temperature of {vessel_with_max_avg_temp['average_temperature']}°C.")
