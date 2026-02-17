from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

RAW_DIR = Path("data/raw")
FIG_DIR = Path("reports/figures")

def main():
    csv_files = list(RAW_DIR.glob("*.csv"))
    if not csv_files:
        raise SystemExit("No CSV files in data/raw. Download data first.")

    df = pd.read_csv(csv_files[0])
    num = df.select_dtypes(include="number")
    if num.shape[1] == 0:
        raise SystemExit("No numeric columns to plot.")

    FIG_DIR.mkdir(parents=True, exist_ok=True)

    col = num.columns[0]
    plt.figure()
    df[col].dropna().plot(kind="hist", bins=30)
    plt.title(f"Histogram: {col}")
    plt.xlabel(col)
    plt.ylabel("Count")
    plt.savefig(FIG_DIR / f"hist_{col}.png", dpi=150, bbox_inches="tight")
    plt.close()

    cols = list(num.columns[:5])
    plt.figure()
    df[cols].plot(kind="box")
    plt.title("Boxplot (first numeric columns)")
    plt.savefig(FIG_DIR / "boxplot_numeric.png", dpi=150, bbox_inches="tight")
    plt.close()

    print("Saved figures to reports/figures/")

if __name__ == "__main__":
    main()
