from utils import get_vessel_list, get_vessel_positions
import matplotlib.pyplot as plt
import numpy as np

def plot_temperature_distribution(year):
    """Plots the temperature distribution for all vessels in the specified year."""
    vessel_ids = get_vessel_list()
    all_temperatures = []  # List to store temperatures from all vessels

    for vessel_id in vessel_ids:
        positions = get_vessel_positions(vessel_id, year)
        
        for pos in positions:
            data = pos.get('data', {})
            seatemp = data.get('seatemp')
            airtemp = data.get('airtemp')
            
            # Only consider temperatures below 70
            if seatemp is not None and airtemp is not None:
                if -70< seatemp < 70 and -70< airtemp < 70:
                    combined_temp = (seatemp + airtemp) / 2
                    all_temperatures.append(combined_temp)

    # Plot the distribution of all valid temperatures
    if all_temperatures:
        plt.figure(figsize=(10, 6))
        plt.hist(all_temperatures, bins=30, color='skyblue', edgecolor='black')
        plt.title(f'Temperature Distribution for All Vessels in {year}')
        plt.xlabel('Temperature (°C)')
        plt.ylabel('Frequency')
        plt.grid(axis='y', alpha=0.75)
        plt.axvline(np.mean(all_temperatures), color='red', linestyle='dashed', linewidth=1,
                    label=f'Average Temp: {round(np.mean(all_temperatures), 2)}°C')
        plt.legend()
        plt.show()
    else:
        print(f"No valid temperature data available for vessels in {year}.")

# Example usage
if __name__ == "__main__":
    year = 2021  # Specify the year
    plot_temperature_distribution(year)
