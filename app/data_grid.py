import dash_ag_grid as dag
from dash import html
import pandas as pd
from app.data_loading import load_sales_data

# Load data
df = load_sales_data('data/sales_data.csv')

def create_data_grid():
    return dag.AgGrid(
        id='sales-data-grid',
        columnDefs=[
            {'headerName': 'Opportunity ID', 'field': 'opportunity_id'},
            {'headerName': 'Sales Agent', 'field': 'sales_agent'},
            {'headerName': 'Product', 'field': 'product'},
            {'headerName': 'Account', 'field': 'account'},
            {'headerName': 'Deal Stage', 'field': 'deal_stage'},
            {'headerName': 'Engage Date', 'field': 'engage_date', 'type': 'dateColumn'},
            {'headerName': 'Close Date', 'field': 'close_date', 'type': 'dateColumn'},
            {'headerName': 'Close Value', 'field': 'close_value', 'type': 'numberColumn'},
            {'headerName': 'Manager', 'field': 'manager'},
            {'headerName': 'Regional Office', 'field': 'regional_office'},
            {'headerName': 'Sector', 'field': 'sector'},
            {'headerName': 'Year Established', 'field': 'year_established', 'type': 'numberColumn'},
            {'headerName': 'Revenue', 'field': 'revenue', 'type': 'numberColumn'},
            {'headerName': 'Employees', 'field': 'employees', 'type': 'numberColumn'},
            {'headerName': 'Office Location', 'field': 'office_location'},
            {'headerName': 'Subsidiary Of', 'field': 'subsidiary_of'},
            {'headerName': 'Series', 'field': 'series'},
            {'headerName': 'Sales Price', 'field': 'sales_price', 'type': 'numberColumn'}
        ],
        rowData=df.to_dict('records'),
        defaultColDef={'sortable': True, 'filter': True, 'resizable': True},
        dashGridOptions={
            "pagination": True,
            "paginationPageSize": 20,
        },
        style={'height': '500px', 'width': '100%'}
    )
