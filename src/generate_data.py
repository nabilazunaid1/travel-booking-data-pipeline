
from pathlib import Path
import pandas as pd

# Step 1: Find the main project folder
BASE_DIR = Path(__file__).resolve().parent.parent

# Step 2: Set the location of the CSV file
RAW_DATA_PATH = BASE_DIR / "data" / "raw" / "bookings.csv"


def generate_sample_data():

    # Step 3: Create sample travel bookings
    bookings = [
        ["B001", "C001", "Tokyo", "2026-01-10", "2026-03-15", 2500, "Confirmed"],
        ["B002", "C002", "Seoul", "2026-01-12", "2026-04-10", 1800, "Confirmed"],
        ["B003", "C003", "Bangkok", "2026-01-15", "2026-02-20", 950, "Cancelled"],
        ["B004", "C001", "Tokyo", "2026-01-18", "2026-05-01", 3200, "Confirmed"],
        ["B005", "C004", "Singapore", "2026-01-20", "2026-03-05", 1200, "Pending"],
        ["B006", "C005", "Bali", "2026-01-22", "2026-04-15", 1750, "Confirmed"],
        ["B007", "C006", "Paris", "2026-01-25", "2026-06-10", 5400, "Confirmed"],
        ["B008", "C007", None, "2026-01-28", "2026-05-20", 2100, "Confirmed"],
        ["B009", "C008", "London", "2026-02-01", "2026-07-01", -500, "Confirmed"],
        ["B010", "C009", "Tokyo", "2026-02-05", "2026-08-10", 2800, "Confirmed"],
        ["B001", "C001", "Tokyo", "2026-01-10", "2026-03-15", 2500, "Confirmed"],
    ]

    # Step 4: Create column names
    columns = [
        "booking_id",
        "customer_id",
        "destination",
        "booking_date",
        "travel_date",
        "amount",
        "status",
    ]

    # Step 5: Convert the data into a pandas DataFrame
    df = pd.DataFrame(bookings, columns=columns)

    # Step 6: Create the destination folder if needed
    RAW_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)

    # Step 7: Save the dataset as a CSV file
    df.to_csv(RAW_DATA_PATH, index=False)

    print("Travel booking dataset created successfully!")
    print(f"File location: {RAW_DATA_PATH}")
    print(f"Total records: {len(df)}")


if __name__ == "__main__":
    generate_sample_data()
