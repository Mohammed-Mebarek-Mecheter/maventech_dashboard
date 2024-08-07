# app\__init__.py
from dash import Dash, html
import dash_bootstrap_components as dbc
from app.layouts import layout
from app.data_grid import create_data_grid

# Initialize the Dash app with a Bootstrap theme
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, 'https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap'])
app.config.suppress_callback_exceptions = True

from app import layouts, callbacks

app.layout = layouts.layout
app.callback = callbacks
app.data_grid = create_data_grid