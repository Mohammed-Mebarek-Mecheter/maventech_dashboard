import dash_bootstrap_components as dbc
from dash import html, dcc

def create_layout(min_date, max_date):
    return html.Div([
        # Sidebar
        html.Div([
            html.H4("Filters", className="filter-title mb-4"),
            dcc.DatePickerRange(
                id='date-range',
                className="mb-3",
                display_format='MMM DD, YYYY',
                start_date=min_date,
                end_date=max_date,
                start_date_placeholder_text='Start',
                end_date_placeholder_text='End',
                style={'backgroundColor': '#041424', 'color': '#FFC107'}
            ),
            dcc.Dropdown(id='regional-office-dropdown', placeholder="Select Regional Office", multi=True, className="filter-dropdown mb-3"),
            dcc.Dropdown(id='sector-dropdown', placeholder="Select Sector", multi=True, className="filter-dropdown mb-3"),
            dcc.Dropdown(id='product-dropdown', placeholder="Select Product", multi=True, className="filter-dropdown mb-3"),
            dcc.Dropdown(id='sales-agent-dropdown', placeholder="Select Sales Agent", multi=True, className="filter-dropdown mb-3"),
        ], className="filter-container", style={"position": "fixed", "top": 0, "left": 0, "bottom": 0, "width": "18rem", "padding": "2rem 1rem"}),

        # Main content
        html.Div([
            html.H1("MavenTech Sales Dashboard", className="text-center mb-4"),

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
        ], style={"margin-left": "20rem", "margin-right": "2rem", "padding": "2rem 1rem", "background-color": "#041424", "color": "#F8F9FA"}),
    ], style={'backgroundColor': '#041424', 'color': '#F8F9FA'})
