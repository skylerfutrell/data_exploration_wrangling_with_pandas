---

## Overview

This project explores and wrangles hourly weather observation data from two Finnish weather stations — **Helsinki Kumpula** and **Rovaniemi** — covering May through August 2017. Using the pandas library, the script performs basic statistical analysis, cleans and transforms the data, filters it by station and date, and exports the results to CSV files.

---

## Files

| File | Description |
|------|-------------|
| `futrell_skyler_data300_data_exploration.py` | Main Python script containing all four parts of the analysis |
| `Kumpula_temps_May_Aug_2017.csv` | Cleaned, filtered output for Helsinki Kumpula (USAF 29980) |
| `Rovaniemi_temps_May_Aug_2017.csv` | Cleaned, filtered output for Rovaniemi (USAF 28450) |

### Input

The script reads from `6153237444115dat.csv`, a raw weather dataset containing multi-station hourly observations. Asterisk values (`*` through `******`) are treated as missing data (NaN).

### Output CSV Columns

| Column | Description |
|--------|-------------|
| `USAF` | Station identifier code |
| `YR--MODAHRMN` | Timestamp in `YYYYMMDDHHmm` format |
| `TEMP` | Temperature in Fahrenheit |
| `MAX` | Daily maximum temperature (Fahrenheit) |
| `MIN` | Daily minimum temperature (Fahrenheit) |
| `Celsius` | Temperature converted to Celsius (rounded to 1 decimal place) |

---

## What the Script Does

### Part 1 – Basic Statistics
Loads the raw CSV and prints summary information: row count, column names, data types, mean Fahrenheit temperature, standard deviation of the MAX column, and the number of unique weather stations.

### Part 2 – Data Manipulation
Selects the five relevant columns, drops rows where `TEMP` is missing, and adds a `Celsius` column converted from Fahrenheit using the formula:

```
Celsius = (Fahrenheit − 32) / 1.8
```

### Part 3 – Data Selection
Filters the cleaned data into two station-specific DataFrames using USAF codes, then saves each to its own CSV file.

### Part 4 – Data Analysis

- **Part 4a:** Computes the median Celsius temperature across the full May–August period for each station.
- **Part 4b:** Computes mean, minimum, and maximum Celsius temperatures for each station during May and June 2017 separately.

---

## Requirements

- Python 3.x
- pandas

Install dependencies with:

```bash
pip install pandas
```

---

## Usage

Place `6153237444115dat.csv` in the same directory as the script, then run:

```bash
python futrell_skyler_data300_data_exploration.py
```

Output CSV files will be written to the same directory.
