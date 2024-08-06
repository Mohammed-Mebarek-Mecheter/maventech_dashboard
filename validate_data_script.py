import pandas as pd
from app.data_loading import load_sales_data, get_summary_stats
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    try:
        # Load and validate the data
        df = load_sales_data('data/sales_data.csv')

        # Log some basic information about the dataset
        logging.info(f"Data shape: {df.shape}")
        logging.info(f"Columns: {', '.join(df.columns)}")

        # Check for missing values
        missing_values = df.isnull().sum()
        if missing_values.sum() > 0:
            logging.warning(f"Missing values found:\n{missing_values[missing_values > 0]}")
        else:
            logging.info("No missing values found.")

        # Check data types
        logging.info(f"Data types:\n{df.dtypes}")

        # Calculate and log summary statistics
        summary_stats = get_summary_stats(df)
        logging.info(f"Summary statistics:\n{summary_stats}")

        logging.info("Data validation completed successfully.")
    except Exception as e:
        logging.error(f"An error occurred during data validation: {str(e)}")

if __name__ == "__main__":
    main()
