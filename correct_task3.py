import pandas as pd
import numpy as np

def average_valid_measurements(values):
    if not isinstance(values, list) or not values:
        return 0.0
    s = pd.Series(values)
    valid_measurements = pd.to_numeric(s, errors='coerce').dropna()

    if valid_measurements.empty:
        return 0.0
    return float(valid_measurements.mean())
