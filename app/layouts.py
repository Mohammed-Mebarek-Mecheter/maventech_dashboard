import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash import html, dcc
from dash_iconify import DashIconify

# Define a consistent color scheme
colors = {
    'background': '#F8F9FA',
    'text': '#212529',
    'primary': '#007BFF',
    'secondary': '#6C757D',
    'success': '#28A745',
    'info': '#17A2B8',
    'warning': '#FFC107',
    'danger': '#DC3545',
}

# Define the layout
layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("MavenTech Sales Dashboard", className="text-center mb-4"), width=12)
    ]),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("Filters", className="card-title filter-title"),
                    dcc.DatePickerRange(id='date-range', className="mb-2", display_format='MMM DD, YYYY', start_date_placeholder_text='Start', end_date_placeholder_text='End'),
                    dcc.Dropdown(id='regional-office-dropdown', placeholder="Select Regional Office", multi=True, className="filter-dropdown"),
                    dcc.Dropdown(id='sector-dropdown', placeholder="Select Sector", multi=True, className="filter-dropdown"),
                    dcc.Dropdown(id='product-dropdown', placeholder="Select Product", multi=True, className="filter-dropdown"),
                    dcc.Dropdown(id='sales-agent-dropdown', placeholder="Select Sales Agent", multi=True, className="filter-dropdown"),
                ], className="filter-container")
            ], className="mb-4")
        ], width=3),

        dbc.Col([
            dbc.Row([
                dbc.Col(dbc.Card(dbc.CardBody([
                    html.H4("Total Revenue", className="card-title"),
                    html.H2(id="total-revenue", className="card-text")
                ]), className="mb-4"), width=3),
                dbc.Col(dbc.Card(dbc.CardBody([
                    html.H4("Deals Closed", className="card-title"),
                    html.H2(id="deals-closed", className="card-text")
                ]), className="mb-4"), width=3),
                dbc.Col(dbc.Card(dbc.CardBody([
                    html.H4("Avg Deal Size", className="card-title"),
                    html.H2(id="avg-deal-size", className="card-text")
                ]), className="mb-4"), width=3),
                dbc.Col(dbc.Card(dbc.CardBody([
                    html.H4("Win Rate", className="card-title"),
                    html.H2(id="win-rate", className="card-text")
                ]), className="mb-4"), width=3),
            ]),
            dbc.Row([
                dbc.Col(dbc.Card(dbc.CardBody([
                    html.H4("Revenue Over Time", className="card-title"),
                    dcc.Graph(id="revenue-over-time-chart")
                ]), className="mb-4"), width=12),
            ]),
            dbc.Row([
                dbc.Col(dbc.Card(dbc.CardBody([
                    html.H4("Sales Pipeline", className="card-title"),
                    dcc.Graph(id="sales-pipeline-chart")
                ]), className="mb-4"), width=6),
                dbc.Col(dbc.Card(dbc.CardBody([
                    html.H4("Top Products", className="card-title"),
                    dcc.Graph(id="top-products-chart")
                ]), className="mb-4"), width=6),
            ]),
        ], width=9)
    ]),

    dbc.Row([
        dbc.Col(dbc.Card(dbc.CardBody([
            html.H4("Sales by Region", className="card-title"),
            dcc.Graph(id="sales-by-region-chart")
        ]), className="mb-4"), width=6),
        dbc.Col(dbc.Card(dbc.CardBody([
            html.H4("Sales Cycle Duration", className="card-title"),
            dcc.Graph(id="sales-cycle-duration-chart")
        ]), className="mb-4"), width=6),
    ]),

    dbc.Row([
        dbc.Col(dbc.Card(dbc.CardBody([
            html.H4("Top Performing Sales Agents", className="card-title"),
            dcc.Graph(id="top-sales-agents-chart")
        ]), className="mb-4"), width=12),
    ]),

], fluid=True, style={'backgroundColor': colors['background'], 'color': colors['text']})
