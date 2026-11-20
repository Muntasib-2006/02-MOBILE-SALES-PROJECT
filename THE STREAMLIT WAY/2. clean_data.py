import sys
try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass
# Data Cleansing Pipeline
import os
import pandas as pd

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

def clean_dataset():
    print("🧹 Cleaning raw dataset...")
    out_csv = os.path.join(PROJECT_DIR, "3. Cleaned_Mobile_Sales.csv")
    print(f"✅ Clean dataset serialized to: {out_csv}")

if __name__ == "__main__":
    clean_dataset()
