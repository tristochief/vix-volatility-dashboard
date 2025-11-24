#!/usr/bin/env python3
"""
Script to download and preprocess VIX data for the dashboard.
Run this before starting the dashboard for the first time.
"""

import pandas as pd
import numpy as np
from datetime import datetime

print("Downloading VIX data from FRED...")
url = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=VIXCLS"
df = pd.read_csv(url)

print(f"Downloaded {len(df)} observations")
print(f"Date range: {df['observation_date'].min()} to {df['observation_date'].max()}")

# Basic preprocessing
df['observation_date'] = pd.to_datetime(df['observation_date'])
df['VIXCLS'] = pd.to_numeric(df['VIXCLS'], errors='coerce')
df = df.sort_values('observation_date').reset_index(drop=True)

# Forward fill missing values
df['VIXCLS'] = df['VIXCLS'].fillna(method='ffill').fillna(method='bfill')

# Add basic features
df['vix_ma_20'] = df['VIXCLS'].rolling(window=20, min_periods=1).mean()
df['vix_ma_60'] = df['VIXCLS'].rolling(window=60, min_periods=1).mean()

# Save preprocessed data
df.to_csv('vix_preprocessed_data.csv', index=False)
print(f"✓ Saved preprocessed data to vix_preprocessed_data.csv")
print(f"✓ Ready to run: streamlit run vix_dashboard.py")
