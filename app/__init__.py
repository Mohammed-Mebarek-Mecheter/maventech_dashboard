import dash
import dash_bootstrap_components as dbc

# Initialize the Dash app with a Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, 'https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap'])
app.config.suppress_callback_exceptions = True

from app import layouts, callbacks

app.layout = layouts.layout
