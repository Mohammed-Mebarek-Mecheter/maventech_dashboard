import unittest
import pandas as pd
from pathlib import Path
from app.data_loading import load_sales_data, validate_data, get_summary_stats

class TestDataLoading(unittest.TestCase):

    def setUp(self):
        # Create a sample DataFrame for testing
        self.sample_data = pd.DataFrame({
            'opportunity_id': ['001', '002', '003'],
            'sales_agent': ['Alice', 'Bob', 'Charlie'],
            'product': ['Product A', 'Product B', 'Product A'],
            'account': ['Acme Inc', 'Beta Corp', 'Gamma Ltd'],
            'deal_stage': ['Won', 'Lost', 'Engaging'],
            'engage_date': pd.to_datetime(['2023-01-01', '2023-02-01', '2023-03-01']),
            'close_date': pd.to_datetime(['2023-01-15', '2023-02-15', '2023-03-15']),
            'close_value': [1000, 2000, 3000],
            'manager': ['Manager1', 'Manager2', 'Manager1'],
            'regional_office': ['North', 'South', 'North'],
            'sector': ['Tech', 'Finance', 'Healthcare'],
            'year_established': [2000, 2010, 2020],
            'revenue': [1000000, 2000000, 3000000],
            'employees': [100, 200, 300],
            'office_location': ['New York', 'London', 'Tokyo'],
            'subsidiary_of': ['Company A', 'Company B', 'Company C'],
            'series': ['Series X', 'Series Y', 'Series Z'],
            'sales_price': [900, 1800, 2700]
        })

        # Save sample data to a temporary CSV file
        self.temp_csv_path = Path('temp_test_data.csv')
        self.sample_data.to_csv(self.temp_csv_path, index=False)

    def tearDown(self):
        # Remove the temporary CSV file
        self.temp_csv_path.unlink()

    def test_load_sales_data(self):
        df = load_sales_data(str(self.temp_csv_path))
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 3)
        self.assertEqual(list(df.columns), list(self.sample_data.columns))

    def test_load_sales_data_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            load_sales_data('non_existent_file.csv')

    def test_validate_data(self):
        # This should not raise any exceptions
        validate_data(self.sample_data)

    def test_validate_data_missing_column(self):
        invalid_data = self.sample_data.drop('opportunity_id', axis=1)
        with self.assertRaises(ValueError):
            validate_data(invalid_data)

    def test_validate_data_invalid_deal_stage(self):
        invalid_data = self.sample_data.copy()
        invalid_data.loc[0, 'deal_stage'] = 'Invalid'
        with self.assertRaises(ValueError):
            validate_data(invalid_data)

    def test_validate_data_negative_value(self):
        invalid_data = self.sample_data.copy()
        invalid_data.loc[0, 'close_value'] = -1000
        with self.assertRaises(ValueError):
            validate_data(invalid_data)

    def test_get_summary_stats(self):
        stats = get_summary_stats(self.sample_data)
        self.assertEqual(stats['total_revenue'], 6000)
        self.assertEqual(stats['total_deals'], 3)
        self.assertEqual(stats['avg_deal_size'], 2000)
        self.assertAlmostEqual(stats['win_rate'], 1/3)
        self.assertEqual(stats['top_product'], 'Product A')
        self.assertEqual(stats['top_sales_agent'], 'Alice')

if __name__ == '__main__':
    unittest.main()
