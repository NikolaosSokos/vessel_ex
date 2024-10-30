
## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository
   ```

2. **Build the Docker Image**
   ```bash
   docker build -t northernmost_vessel_app .
   ```

3. **Run the Docker Container**:
   - For Northernmost Vessel
     ```bash
     docker run northernmost_vessel_app --task north --year 2021
     ```
   - For Highest Average Temperature Vessel
     ```bash
     docker run northernmost_vessel_app --task temp --year 2021
     ```

## Usage

The script can be run to perform one of two tasks: find the northernmost vessel or find the vessel with the highest average temperature for a given year. By default, the year is set to 2021.

### Command-Line Arguments

The script accepts the following command-line arguments:

- `--task`: Specifies the analysis task to perform. Options:
  - `north`: Find the northernmost vessel.
  - `temp`: Find the vessel with the highest average temperature.
  
- `--year`: Optional. Specify the year for analysis. If omitted, the default year is 2021.

### Examples

1. **Finding the Northernmost Vessel in 2021**:
   ```bash
   python main.py --task north --year 2021

2. **Finding the Vessel with Maximum Average Temperature in 2020:**:
   ```bash
   python main.py --task temp --year 2020
