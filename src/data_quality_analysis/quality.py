from pathlib import Path
import json
import pandas as pd

RAW_DIR = Path("data/raw")
REPORTS_DIR = Path("reports")

def main():
    csv_files = list(RAW_DIR.glob("*.csv"))
    if not csv_files:
        raise SystemExit("No CSV files in data/raw. Download data first.")

    df = pd.read_csv(csv_files[0])

    report = {
        "rows": int(df.shape[0]),
        "cols": int(df.shape[1]),
        "missing_by_column": df.isna().sum().sort_values(ascending=False).to_dict(),
        "duplicate_rows": int(df.duplicated().sum()),
        "dtypes": df.dtypes.astype(str).to_dict(),
    }

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    out = REPORTS_DIR / "data_quality_report.json"
    with open(out, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print(f"Saved: {out}")

if __name__ == "__main__":
    main()
