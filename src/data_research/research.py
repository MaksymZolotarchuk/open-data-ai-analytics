from pathlib import Path
import pandas as pd

RAW_DIR = Path("data/raw")
REPORTS_DIR = Path("reports")

def main():
    csv_files = list(RAW_DIR.glob("*.csv"))
    if not csv_files:
        raise SystemExit("No CSV files in data/raw. Download data first.")

    df = pd.read_csv(csv_files[0])

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    desc = df.describe(include="all").transpose()
    desc.to_csv(REPORTS_DIR / "eda_describe.csv", index=True)
    print("Saved: reports/eda_describe.csv")

    num = df.select_dtypes(include="number")
    if num.shape[1] >= 2:
        corr = num.corr(numeric_only=True)
        corr.to_csv(REPORTS_DIR / "correlation.csv")
        print("Saved: reports/correlation.csv")
    else:
        print("Not enough numeric columns for correlation.")

if __name__ == "__main__":
    main()
