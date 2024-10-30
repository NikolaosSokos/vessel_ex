import argparse
from vessel_north import find_northernmost_vessel
from vessel_temperature import find_max_average_temp_vessel

def main():
    parser = argparse.ArgumentParser(description="Vessel Data Analysis")
    parser.add_argument("--year", type=int, default=2021, help="Specify the year to analyze (default is 2021)")
    parser.add_argument("--task", choices=["north", "temp"], required=True, 
                        help="Choose 'north' to find northernmost vessel or 'temp' for max average temperature vessel")
    
    args = parser.parse_args()
    
    if args.task == "north":
        find_northernmost_vessel(args.year)
    elif args.task == "temp":
        find_max_average_temp_vessel(args.year)

if __name__ == "__main__":
    main()
