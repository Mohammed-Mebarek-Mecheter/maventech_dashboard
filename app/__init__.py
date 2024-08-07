# app/__init__.py
from dash import Dash, html
import dash_bootstrap_components as dbc
from app.layouts import create_layout
from app.data_loading import load_sales_data

# Load data
df = load_sales_data('data/sales_data.csv')

# Get min and max dates
min_date = df['close_date'].min()
max_date = df['close_date'].max()

# Initialize the Dash app with a Bootstrap theme and custom CSS
external_stylesheets = [
    dbc.themes.BOOTSTRAP,
    'https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap',
    '/assets/custom.css'  # Path to the custom CSS file
]

app = Dash(__name__, external_stylesheets=external_stylesheets)
app.config.suppress_callback_exceptions = True

from app import layouts, callbacks

# Set layout with min and max dates
app.layout = create_layout(min_date=min_date, max_date=max_date)
app.callback = callbacks
