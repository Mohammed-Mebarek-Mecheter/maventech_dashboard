import pandas as pd
import numpy as np
from typing import Dict, Any
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_sales_data(file_path: str) -> pd.DataFrame:
    try:
        logging.info(f"Loading data from {file_path}")
        df = pd.read_csv(file_path, parse_dates=['engage_date', 'close_date'])

        # Perform data validation
        validate_data(df)

        # Perform data preprocessing
        df = preprocess_data(df)

        logging.info("Data loaded, validated, and preprocessed successfully")
        return df
    except Exception as e:
        logging.error(f"Error loading data: {str(e)}")
        raise

def validate_data(df: pd.DataFrame) -> None:
    expected_columns = [
        'opportunity_id', 'sales_agent', 'product', 'account', 'deal_stage',
        'engage_date', 'close_date', 'close_value', 'manager', 'regional_office',
        'sector', 'year_established', 'revenue', 'employees', 'office_location',
        'subsidiary_of', 'series', 'sales_price'
    ]

    # Check for required columns
    missing_columns = set(expected_columns) - set(df.columns)
    if missing_columns:
        raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")

    # Check data types
    if not pd.api.types.is_datetime64_any_dtype(df['engage_date']):
        raise ValueError("Column 'engage_date' should be datetime")
    if not pd.api.types.is_datetime64_any_dtype(df['close_date']):
        raise ValueError("Column 'close_date' should be datetime")

    # Check for non-negative numerical values
    for col in ['close_value', 'year_established', 'revenue', 'employees', 'sales_price']:
        if (df[col] < 0).any():
            raise ValueError(f"Column '{col}' contains negative values")

    # Check for valid deal stages
    valid_deal_stages = {'Prospecting', 'Engaging', 'Won', 'Lost'}
    invalid_stages = set(df['deal_stage'].unique()) - valid_deal_stages
    if invalid_stages:
        raise ValueError(f"Invalid deal stages found: {', '.join(invalid_stages)}")

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    # Calculate sales cycle duration
    df['sales_cycle_duration'] = (df['close_date'] - df['engage_date']).dt.days

    # Create quarter and year columns
    df['quarter'] = df['close_date'].dt.to_period('Q')
    df['year'] = df['close_date'].dt.year

    # Calculate win rate
    df['is_won'] = df['deal_stage'] == 'Won'

    # Calculate deal size category
    df['deal_size_category'] = pd.cut(df['close_value'],
                                      bins=[0, 1000, 5000, 10000, np.inf],
                                      labels=['Small', 'Medium', 'Large', 'Enterprise'])

    return df

def get_summary_stats(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        'total_revenue': df['close_value'].sum(),
        'total_deals': len(df),
        'avg_deal_size': df['close_value'].mean(),
        'win_rate': df['is_won'].mean(),
        'top_product': df['product'].value_counts().index[0],
        'top_sales_agent': df['sales_agent'].value_counts().index[0],
        'avg_sales_cycle': df['sales_cycle_duration'].mean()
    }

if __name__ == "__main__":
    try:
        sales_df = load_sales_data('data/sales_data.csv')
        summary_stats = get_summary_stats(sales_df)
        logging.info(f"Summary Statistics: {summary_stats}")
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
