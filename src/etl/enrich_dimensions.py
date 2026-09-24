#!/usr/bin/env python3
"""
Dimension Enrichment Module: Adds GPS coordinates, FAA Hub tiers, timezones to dim_airport.csv
and weekend/holiday metadata to dim_date.csv.
"""
import pandas as pd
import numpy as np
import datetime
import os

def get_faa_hub_and_coords():
    """Returns mapping of common IATA airport codes to (lat, lon, hub_category, timezone)."""
    hubs = {
        'ATL': (33.6407, -84.4277, 'Large Hub', 'America/New_York'),
        'DFW': (32.8998, -97.0403, 'Large Hub', 'America/Chicago'),
        'DEN': (39.8561, -104.6737, 'Large Hub', 'America/Denver'),
        'ORD': (41.9742, -87.9073, 'Large Hub', 'America/Chicago'),
        'CLT': (35.2140, -80.9431, 'Large Hub', 'America/New_York'),
        'LAX': (33.9416, -118.4085, 'Large Hub', 'America/Los_Angeles'),
        'JFK': (40.6413, -73.7781, 'Large Hub', 'America/New_York'),
        'LAS': (36.0840, -115.1537, 'Large Hub', 'America/Los_Angeles'),
        'MCO': (28.4312, -81.3081, 'Large Hub', 'America/New_York'),
        'SEA': (47.4502, -122.3088, 'Large Hub', 'America/Los_Angeles'),
        'MIA': (25.7959, -80.2870, 'Large Hub', 'America/New_York'),
        'EWR': (40.6895, -74.1745, 'Large Hub', 'America/New_York'),
        'SFO': (37.6213, -122.3790, 'Large Hub', 'America/Los_Angeles'),
        'PHX': (33.4342, -112.0080, 'Large Hub', 'America/Phoenix'),
        'IAH': (29.9902, -95.3368, 'Large Hub', 'America/Chicago'),
        'BOS': (42.3656, -71.0096, 'Large Hub', 'America/New_York'),
        'MSP': (44.8848, -93.2223, 'Large Hub', 'America/Chicago'),
        'DTW': (42.2162, -83.3554, 'Large Hub', 'America/New_York'),
        'FLL': (26.0742, -80.1506, 'Large Hub', 'America/New_York'),
        'PHL': (39.8729, -75.2437, 'Large Hub', 'America/New_York'),
        'BWI': (39.1774, -76.6684, 'Large Hub', 'America/New_York'),
        'SLC': (40.7899, -111.9791, 'Large Hub', 'America/Denver'),
        'SAN': (32.7338, -117.1933, 'Large Hub', 'America/Los_Angeles'),
        'IAD': (38.9531, -77.4565, 'Large Hub', 'America/New_York'),
        'BNA': (36.1263, -86.6774, 'Large Hub', 'America/Chicago'),
        'TPA': (27.9755, -82.5332, 'Large Hub', 'America/New_York'),
        'MDW': (41.7868, -87.7522, 'Large Hub', 'America/Chicago'),
        'PDX': (45.5898, -122.5951, 'Large Hub', 'America/Los_Angeles'),
        'STL': (38.7472, -90.3599, 'Medium Hub', 'America/Chicago'),
        'HOU': (29.6454, -95.2789, 'Medium Hub', 'America/Chicago'),
        'DAL': (32.8471, -96.8518, 'Medium Hub', 'America/Chicago'),
        'AUS': (30.1975, -97.6664, 'Large Hub', 'America/Chicago'),
        'SMF': (38.6954, -121.5908, 'Medium Hub', 'America/Los_Angeles'),
        'RDU': (35.8801, -78.7880, 'Medium Hub', 'America/New_York'),
        'MSY': (29.9911, -90.2580, 'Medium Hub', 'America/Chicago'),
        'SJC': (37.3639, -121.9289, 'Medium Hub', 'America/Los_Angeles'),
        'PIT': (40.4915, -80.2329, 'Medium Hub', 'America/New_York'),
        'SAT': (29.5337, -98.4698, 'Medium Hub', 'America/Chicago'),
        'CLE': (41.4058, -81.8539, 'Medium Hub', 'America/New_York'),
        'IND': (39.7173, -86.2944, 'Medium Hub', 'America/New_York'),
        'CMH': (39.9980, -82.8919, 'Medium Hub', 'America/New_York'),
        'CVG': (39.0461, -84.6622, 'Medium Hub', 'America/New_York'),
        'MKE': (42.9475, -87.8966, 'Medium Hub', 'America/Chicago'),
        'BDL': (41.9389, -72.6832, 'Medium Hub', 'America/New_York'),
        'JAX': (30.4941, -81.6879, 'Medium Hub', 'America/New_York'),
        'RSW': (26.5362, -81.7552, 'Medium Hub', 'America/New_York'),
        'OAK': (37.7213, -122.2207, 'Medium Hub', 'America/Los_Angeles'),
        'MEM': (35.0424, -89.9767, 'Medium Hub', 'America/Chicago'),
        'BUF': (42.9405, -78.7322, 'Medium Hub', 'America/New_York'),
        'ABQ': (35.0402, -106.6092, 'Medium Hub', 'America/Denver'),
        'OMA': (41.3025, -95.8942, 'Medium Hub', 'America/Chicago'),
        'PBI': (26.6832, -80.0956, 'Medium Hub', 'America/New_York'),
        'ANC': (61.1743, -149.9962, 'Medium Hub', 'America/Anchorage'),
        'HNL': (21.3187, -157.9224, 'Large Hub', 'Pacific/Honolulu'),
    }
    return hubs

def enrich_airport_dimension(filepath="dimensions/dim_airport.csv"):
    """Enriches dim_airport.csv with lat, lon, faaHubCategory, and timeZone."""
    df = pd.read_csv(filepath)
    hubs = get_faa_hub_and_coords()
    
    lats, lons, categories, timezones = [], [], [], []
    for _, row in df.iterrows():
        code = str(row['airportCode']).strip()
        if code == 'UNKNOWN' or row['airportId'] == 0:
            lats.append(np.nan)
            lons.append(np.nan)
            categories.append('UNKNOWN')
            timezones.append('UNKNOWN')
        elif code in hubs:
            lat, lon, cat, tz = hubs[code]
            lats.append(lat)
            lons.append(lon)
            categories.append(cat)
            timezones.append(tz)
        else:
            lats.append(np.nan)
            lons.append(np.nan)
            categories.append('Non-Hub / Regional')
            timezones.append('America/New_York')
            
    df['latitude'] = lats
    df['longitude'] = lons
    df['faaHubCategory'] = categories
    df['timeZone'] = timezones
    
    df.to_csv(filepath, index=False)
    print(f"Successfully enriched {filepath} with {len(df)} rows and 4 new columns!")

def get_us_holidays(years=range(2019, 2027)):
    """Returns dictionary of date strings -> holiday name."""
    holidays = {}
    for y in years:
        holidays[f"{y}-01-01"] = "New Year's Day"
        holidays[f"{y}-07-04"] = "Independence Day"
        holidays[f"{y}-11-11"] = "Veterans Day"
        holidays[f"{y}-12-25"] = "Christmas Day"
        
        mlk = [d for d in [datetime.date(y, 1, i) for i in range(1, 32)] if d.weekday() == 0][2]
        holidays[str(mlk)] = "MLK Jr. Day"
        
        pres = [d for d in [datetime.date(y, 2, i) for i in range(1, 29)] if d.weekday() == 0][2]
        holidays[str(pres)] = "Presidents' Day"
        
        mem = [d for d in [datetime.date(y, 5, i) for i in range(1, 32)] if d.weekday() == 0][-1]
        holidays[str(mem)] = "Memorial Day"
        
        if y >= 2021:
            holidays[f"{y}-06-19"] = "Juneteenth"
            
        lab = [d for d in [datetime.date(y, 9, i) for i in range(1, 31)] if d.weekday() == 0][0]
        holidays[str(lab)] = "Labor Day"
        
        col = [d for d in [datetime.date(y, 10, i) for i in range(1, 32)] if d.weekday() == 0][1]
        holidays[str(col)] = "Columbus Day"
        
        thx = [d for d in [datetime.date(y, 11, i) for i in range(1, 31)] if d.weekday() == 3][3]
        holidays[str(thx)] = "Thanksgiving Day"
        
    return holidays

def enrich_date_dimension(filepath="dimensions/dim_date.csv"):
    """Enriches dim_date.csv with isWeekend, isHoliday, and holidayName."""
    df = pd.read_csv(filepath)
    holidays = get_us_holidays()
    
    is_weekends, is_hols, hol_names = [], [], []
    for _, row in df.iterrows():
        dt_str = str(row['date']).strip()
        dow = int(row['dayOfWeek'])
        
        is_weekends.append(1 if dow in (6, 7) else 0)
        
        if dt_str in holidays:
            is_hols.append(1)
            hol_names.append(holidays[dt_str])
        else:
            is_hols.append(0)
            hol_names.append("None")
            
    df['isWeekend'] = is_weekends
    df['isHoliday'] = is_hols
    df['holidayName'] = hol_names
    
    df.to_csv(filepath, index=False)
    print(f"Successfully enriched {filepath} with {len(df)} rows and 3 new columns!")

if __name__ == '__main__':
    enrich_airport_dimension()
    enrich_date_dimension()
