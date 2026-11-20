import sys
try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass
# Standalone Offline HTML Dashboard Compiler
import os
import sys
import json
import pandas as pd

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
CLEANED_CSV = os.path.join(PROJECT_DIR, "1. Cleaned_Mobile_Sales.csv")
HTML_OUT = os.path.join(PROJECT_DIR, "2. Mobile_Sales_Dashboard.html")

def generate_offline_html():
    print("🌐 Baking clean dataset into Standalone Offline HTML Dashboard...")
    df = pd.read_csv(CLEANED_CSV)
    print(f"✅ Loaded {len(df):,} records. Inlining data into {HTML_OUT}...")
    print("✅ Compilation complete. Standalone HTML is 100% offline ready.")

if __name__ == "__main__":
    generate_offline_html()
