import os
from pathlib import Path
import requests

RAW_DIR = Path("data/raw")

def download_file(url: str, out_path: Path, chunk_size: int = 1024 * 1024) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with requests.get(url, stream=True, timeout=60) as r:
        r.raise_for_status()
        with open(out_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=chunk_size):
                if chunk:
                    f.write(chunk)

def main():
    url = os.environ.get("DATA_URL", "").strip()
    if not url:
        raise SystemExit("Set DATA_URL env var with direct resource URL from data.gov.ua")

    filename = os.environ.get("DATA_FILENAME", "dataset.csv")
    out_path = RAW_DIR / filename

    download_file(url, out_path)
    print(f"Saved to: {out_path}")

if __name__ == "__main__":
    main()
