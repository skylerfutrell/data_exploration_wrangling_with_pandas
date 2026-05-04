# =============================================================================
# PART 1 - Basic statistics of the data
# =============================================================================

import pandas as pd

# Read the CSV file into a DataFrame called 'data'
# na_values tells pandas to treat all * variants as NaN (missing data)
data = pd.read_csv(
    '6153237444115dat.csv',
    na_values=['*', '**', '***', '****', '*****', '******']
)

# How many rows are there in the data?
print("Number of rows:", len(data))

# What are the column names?
print("\nColumn names:")
print(list(data.columns))

# What are the datatypes of the columns?
print("\nColumn datatypes:")
print(data.dtypes)

# What is the mean Fahrenheit temperature in the data? (TEMP column)
print("\nMean temperature (Fahrenheit):", round(data['TEMP'].mean(), 2))

# What is the standard deviation of the Maximum temperature? (MAX column)
print("Standard deviation of MAX temperature:", round(data['MAX'].std(), 2))

# How many unique stations exist in the data? (USAF column)
print("Number of unique stations:", data['USAF'].nunique())


# =============================================================================
# PART 2 - Data manipulation
# =============================================================================

# Select only the relevant columns into a new variable called 'selected'
selected = data[['USAF', 'YR--MODAHRMN', 'TEMP', 'MAX', 'MIN']].copy()

# Remove all rows where TEMP has a NaN (NoData) value
selected = selected.dropna(subset=['TEMP'])

# Convert TEMP from Fahrenheit to Celsius using formula: C = (F - 32) / 1.8
# Store result in a new column called 'Celsius', rounded to 1 decimal place
selected['Celsius'] = ((selected['TEMP'] - 32) / 1.8).round(1)


# =============================================================================
# PART 3 - Data selection
# =============================================================================

# Select rows for Helsinki Kumpula (USAF code 29980)
kumpula = selected[selected['USAF'] == 29980].copy()

# Select rows for Rovaniemi (USAF code 28450)
rovaniemi = selected[selected['USAF'] == 28450].copy()

# Save kumpula DataFrame to a CSV file with comma separator and 1 decimal place
kumpula.to_csv(
    'Kumpula_temps_May_Aug_2017.csv',
    sep=',',
    float_format='%.1f',
    index=False
)

# Save rovaniemi DataFrame to a CSV file with comma separator and 1 decimal place
rovaniemi.to_csv(
    'Rovaniemi_temps_May_Aug_2017.csv',
    sep=',',
    float_format='%.1f',
    index=False
)

print("\nCSV files saved successfully.")


# =============================================================================
# PART 4 - Data analysis
# =============================================================================

# --- Part 4a: Median temperatures for the full dataset (May-Aug) ---

# Median Celsius temperature for Helsinki Kumpula
kumpula_median = kumpula['Celsius'].median()
print("\nPart 4a:")
print(f"Helsinki Kumpula median temperature (Celsius): {kumpula_median:.1f}")

# Median Celsius temperature for Rovaniemi
rovaniemi_median = rovaniemi['Celsius'].median()
print(f"Rovaniemi median temperature (Celsius): {rovaniemi_median:.1f}")


# --- Part 4b: Mean, min, max temperatures for May and June separately ---

# Select May 2017 rows (YR--MODAHRMN between 201705010000 and 201705312359)
kumpula_may = kumpula[
    (kumpula['YR--MODAHRMN'] >= 201705010000) &
    (kumpula['YR--MODAHRMN'] < 201706010000)
]
rovaniemi_may = rovaniemi[
    (rovaniemi['YR--MODAHRMN'] >= 201705010000) &
    (rovaniemi['YR--MODAHRMN'] < 201706010000)
]

# Select June 2017 rows
kumpula_june = kumpula[
    (kumpula['YR--MODAHRMN'] >= 201706010000) &
    (kumpula['YR--MODAHRMN'] < 201707010000)
]
rovaniemi_june = rovaniemi[
    (rovaniemi['YR--MODAHRMN'] >= 201706010000) &
    (rovaniemi['YR--MODAHRMN'] < 201707010000)
]

# Print mean, min, and max temperatures for Kumpula in May and June
print("\nPart 4b:")
print(f"Kumpula May    -> Mean: {kumpula_may['Celsius'].mean():.1f} °C  |  "
      f"Min: {kumpula_may['Celsius'].min():.1f} °C  |  "
      f"Max: {kumpula_may['Celsius'].max():.1f} °C")

print(f"Kumpula June   -> Mean: {kumpula_june['Celsius'].mean():.1f} °C  |  "
      f"Min: {kumpula_june['Celsius'].min():.1f} °C  |  "
      f"Max: {kumpula_june['Celsius'].max():.1f} °C")

# Print mean, min, and max temperatures for Rovaniemi in May and June
print(f"Rovaniemi May  -> Mean: {rovaniemi_may['Celsius'].mean():.1f} °C  |  "
      f"Min: {rovaniemi_may['Celsius'].min():.1f} °C  |  "
      f"Max: {rovaniemi_may['Celsius'].max():.1f} °C")

print(f"Rovaniemi June -> Mean: {rovaniemi_june['Celsius'].mean():.1f} °C  |  "
      f"Min: {rovaniemi_june['Celsius'].min():.1f} °C  |  "
      f"Max: {rovaniemi_june['Celsius'].max():.1f} °C")
