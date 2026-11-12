import csv
import json
import os
import time
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "hr_data.csv"
OUTPUT_DIR = BASE_DIR / "output"


def prepare_paths():
    """Prepare output directory and file paths."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    if not DATA_FILE.exists():
        print(f"Data file {DATA_FILE} does not exist. Please check the path.")
        return False
    print(f"Data file {DATA_FILE} found. Proceeding with report generation.")
    return True
