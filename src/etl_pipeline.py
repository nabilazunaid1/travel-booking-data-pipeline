
from pathlib import Path
import logging
import pandas as pd

# =====================================
# STEP 1: CONFIGURATION
# =====================================

# Locate the main project folder
BASE_DIR = Path(__file__).resolve().parent.parent

# Define input and output file paths
RAW_PATH = BASE_DIR / "data" / "raw" / "bookings.csv"
OUTPUT_PATH = BASE_DIR / "data" / "processed" / "clean_bookings.csv"

# Define the columns we expect in our dataset
REQUIRED_COLUMNS = [
    "booking_id",
    "customer_id",
    "destination",
    "booking_date",
    "travel_date",
    "amount",
    "status",
]

# Allowed booking statuses
VALID_STATUSES = {"Confirmed", "Pending", "Cancelled"}

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


# =====================================
# STEP 2: EXTRACT
# =====================================

def extract():
    """Read booking data from the raw CSV file."""

    logger.info("Starting extraction")

    # Check whether the CSV file exists
    if not RAW_PATH.exists():
        raise FileNotFoundError(
            f"Raw data file not found: {RAW_PATH}"
        )

    # Read CSV into a pandas DataFrame
    df = pd.read_csv(
        RAW_PATH,
        dtype={
            "booking_id": "string",
            "customer_id": "string"
        }
    )

    # Check that all required columns exist
    missing_columns = set(REQUIRED_COLUMNS) - set(df.columns)

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {sorted(missing_columns)}"
        )

    logger.info("Extracted %s raw records", len(df))

    return df


# =====================================
# STEP 3: TRANSFORM
# =====================================

def transform(df):
    """Clean and validate travel booking records."""

    logger.info("Starting transformation")

    # Create a copy to protect the original data
    df = df.copy()

    # Clean extra spaces from text values
    text_columns = [
        "booking_id",
        "customer_id",
        "destination",
        "status"
    ]

    for column in text_columns:
        df[column] = df[column].astype("string").str.strip()

    # Remove duplicate booking IDs
    duplicate_count = df.duplicated(
        subset=["booking_id"]
    ).sum()

    df = df.drop_duplicates(
        subset=["booking_id"],
        keep="first"
    )

    logger.info(
        "Removed %s duplicate records",
        duplicate_count
    )

    # Convert booking amounts to numbers
    df["amount"] = pd.to_numeric(
        df["amount"],
        errors="coerce"
    )

    # Convert dates to datetime values
    df["booking_date"] = pd.to_datetime(
        df["booking_date"],
        format="%Y-%m-%d",
        errors="coerce"
    )

    df["travel_date"] = pd.to_datetime(
        df["travel_date"],
        format="%Y-%m-%d",
        errors="coerce"
    )

    # Validate required fields
    valid_records = (
        df["booking_id"].notna()
        & df["booking_id"].ne("").fillna(False)
        & df["customer_id"].notna()
        & df["customer_id"].ne("").fillna(False)
        & df["destination"].notna()
        & df["destination"].ne("").fillna(False)
        & df["booking_date"].notna()
        & df["travel_date"].notna()
        & (df["travel_date"] >= df["booking_date"])
        & (df["amount"] > 0).fillna(False)
        & df["status"].isin(VALID_STATUSES)
    )

    # Count invalid records before removing them
    invalid_count = (~valid_records).sum()

    # Keep only valid rows
    df = df.loc[valid_records].copy()

    logger.info(
        "Rejected %s invalid records",
        invalid_count
    )

    logger.info(
        "Transformation completed: %s valid records",
        len(df)
    )

    return df


# =====================================
# STEP 4: LOAD
# =====================================

def load(df):
    """Save the cleaned dataset to a CSV file."""

    logger.info("Starting load")

    # Create processed folder if necessary
    OUTPUT_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    # Save cleaned records
    df.to_csv(
        OUTPUT_PATH,
        index=False,
        date_format="%Y-%m-%d"
    )

    logger.info(
        "Loaded %s records into %s",
        len(df),
        OUTPUT_PATH
    )


# =====================================
# STEP 5: RUN THE FULL ETL PIPELINE
# =====================================

def run_pipeline():
    """Execute Extract, Transform, and Load."""

    logger.info("ETL pipeline started")

    try:
        # Extract
        raw_df = extract()

        # Transform
        clean_df = transform(raw_df)

        # Load
        load(clean_df)

        logger.info(
            "ETL pipeline completed successfully"
        )

    except Exception:
        logger.exception("ETL pipeline failed")
        raise


# This section runs only when the script
# is executed directly
if __name__ == "__main__":
    run_pipeline()
