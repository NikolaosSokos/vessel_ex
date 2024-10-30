
# Vessel Data Analysis

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/NikolaosSokos/vessel_ex.git
   cd vessel_ex
   ```

2. **Build the Docker Image**
   ```bash
   docker build -t vessel_app .
   ```

3. **Run the Docker Container**:
   - For finding the northernmost vessel:
     ```bash
     docker run vessel_app --task north --year 2021
     ```
   - For finding the vessel with the highest average sea temperature:
     ```bash
     docker run vessel_app --task temp --year 2021
     ```

## Scripts Overview

### 1. `main.py`

**Functionality**: The main entry point of the application. It allows users to specify which task to run (finding the northernmost vessel or the vessel with the highest average temperature) and the year for the analysis.

**Usage**:
```bash
python main.py --task <task_name> --year <year>
```

**Arguments**:
- `--task`: Specify the task to perform (`north` or `temp`).
- `--year`: Specify the year for analysis (default is 2021).

### 2. `vessel_north.py`

**Functionality**: Contains logic to find the northernmost vessel for the specified year. It calculates the highest latitude reached by each vessel.


### 3. `vessel_temperature.py`

**Functionality**: Contains logic to find the vessel with the highest average temperature based on `seatemp` values for the specified year. It filters out temperatures below -5°C and above 30°C .


## API Utility Functions

The project includes several utility functions to interact with the POSNAV API:

### 1. `get_vessel_list()`

Retrieves a list of all vessel IDs from the API.

### 2. `year_to_iso8601(year)`

Converts a given year into ISO 8601 formatted start and end dates.

### 3. `get_vessel_positions(vessel_id, year)`

Fetches position data for a specific vessel over the specified year.

## Sample Output

- **Finding the Northernmost Vessel**:
  ## Script
  ```bash
  python main.py --task north --year 2021
  ```
  ## Output
  ```plaintext
  The northernmost vessel in 2021 is AT at latitude 64.917 on 2021-07-23T08:34:59.000+0000.
  ```

- **Finding the Vessel with Maximum Average Temperature**:
   ## Script
  ```bash
  python main.py --task temp --year 2021
  ```
  ## Output
  ```plaintext
  The vessel with the highest average temperature in 2021 is AN with an average temperature of 26.54°C.
  ```

