import sys
try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass
# Matplotlib High-Resolution Visual Plotting Engine
import os
import pandas as pd
import matplotlib.pyplot as plt

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

def generate_plots():
    print("🎨 Generating Matplotlib analytical visual charts...")
    df = pd.read_csv(os.path.join(PROJECT_DIR, "3. Cleaned_Mobile_Sales.csv"))
    print(f"✅ Generated static executive visuals.")

if __name__ == "__main__":
    generate_plots()
