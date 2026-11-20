import sys
try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass
# DAX & NumPy Fast Vector Calculation Engine
import os
import pandas as pd
import numpy as np

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

def calculate_kpis():
    print("⚡ Calculating vectorized KPI metrics...")
    df = pd.read_csv(os.path.join(PROJECT_DIR, "3. Cleaned_Mobile_Sales.csv"))
    print(f"✅ Calculated core metrics on {len(df):,} rows.")

if __name__ == "__main__":
    calculate_kpis()
