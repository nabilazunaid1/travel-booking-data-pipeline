
import unittest
import pandas as pd

from src.etl_pipeline import transform


class TestETLPipeline(unittest.TestCase):
    """Automated tests for travel booking ETL logic."""

    def setUp(self):
        """
        Create a valid sample booking before every test.
        Each test gets a fresh copy of this data.
        """
        self.valid_booking = {
            "booking_id": "B001",
            "customer_id": "C001",
            "destination": "Tokyo",
            "booking_date": "2026-01-10",
            "travel_date": "2026-03-15",
            "amount": 2500,
            "status": "Confirmed",
        }

    def make_dataframe(self, **changes):
        """Create a one-row DataFrame with optional changes."""
        booking = self.valid_booking.copy()
        booking.update(changes)
        return pd.DataFrame([booking])

    # TEST 1
    def test_valid_booking(self):
        """A valid booking should remain in the output."""
        df = self.make_dataframe()

        result = transform(df)

        self.assertEqual(len(result), 1)
        self.assertEqual(result.iloc[0]["booking_id"], "B001")

    # TEST 2
    def test_duplicate_booking_removed(self):
        """Duplicate booking IDs should be removed."""
        df = pd.DataFrame([
            self.valid_booking,
            self.valid_booking.copy(),
        ])

        result = transform(df)

        self.assertEqual(len(result), 1)
        self.assertEqual(
            result["booking_id"].duplicated().sum(),
            0
        )

    # TEST 3
    def test_missing_destination_rejected(self):
        """Bookings without a destination should be rejected."""
        df = self.make_dataframe(destination=None)

        result = transform(df)

        self.assertEqual(len(result), 0)

    # TEST 4
    def test_negative_amount_rejected(self):
        """Bookings with negative amounts should be rejected."""
        df = self.make_dataframe(amount=-500)

        result = transform(df)

        self.assertEqual(len(result), 0)

    # TEST 5
    def test_invalid_travel_date_rejected(self):
        """Travel dates before booking dates are invalid."""
        df = self.make_dataframe(
            booking_date="2026-06-10",
            travel_date="2026-05-01"
        )

        result = transform(df)

        self.assertEqual(len(result), 0)

    # TEST 6
    def test_invalid_status_rejected(self):
        """Unknown booking statuses should be rejected."""
        df = self.make_dataframe(status="Unknown")

        result = transform(df)

        self.assertEqual(len(result), 0)


if __name__ == "__main__":
    unittest.main()
