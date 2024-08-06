# data_processing.py
import pandas as pd
import numpy as np

from app.callbacks import df


def load_data():
    df = pd.read_csv('data/sales_data.csv')
    df['engage_date'] = pd.to_datetime(df['engage_date'])
    df['close_date'] = pd.to_datetime(df['close_date'])
    return df

def filter_data(df, start_date, end_date, region, sector, product):
    mask = (df['close_date'] >= start_date) & (df['close_date'] <= end_date)
if region:
    mask &= df['regional_office'] == region
if sector:
    mask &= df['sector'] == sector
if product:
    mask &= df['product'] == product
return df[mask]

def calculate_total_revenue(df):
    return df['close_value'].sum()

def calculate_deals_closed(df):
    return df[df['deal_stage'] == 'Won'].shape[0]

def calculate_avg_deal_size(df):
    return df[df['deal_stage'] == 'Won']['close_value'].mean()

def get_revenue_over_time(df):
    return df.groupby('close_date')['close_value'].sum().reset_index()

def calculate_conversion_rate(df):
    engaged = df[df['deal_stage'] == 'Engaging'].shape[0]
    won = df[df['deal_stage'] == 'Won'].shape[0]
    return won / engaged if engaged > 0 else 0

def get_quarterly_revenue(df):
    df['quarter'] = df['close_date'].dt.to_period('Q')
    return df.groupby('quarter')['close_value'].sum().reset_index()

def get_avg_deal_size_by_product(df):
    return df[df['deal_stage'] == 'Won'].groupby('product')['close_value'].mean().reset_index()

def calculate_avg_sales_cycle(df):
    df['sales_cycle'] = (df['close_date'] - df['engage_date']).dt.days
    return df[df['deal_stage'] == 'Won']['sales_cycle'].mean()

def get_sales_cycle_distribution(df):
    df['sales_cycle'] = (df['close_date'] - df['engage_date']).dt.days
    return df[df['deal_stage'] == 'Won']['sales_cycle']
