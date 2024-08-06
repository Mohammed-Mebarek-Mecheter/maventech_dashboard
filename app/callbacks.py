from dash import Input, Output, State
import plotly.express as px
from app import app
from app.data_loading import load_sales_data

# Load data
df = load_sales_data('data/sales_data.csv')

# Callback for updating dropdown options
@app.callback(
    [Output('regional-office-dropdown', 'options'),
     Output('sector-dropdown', 'options'),
     Output('product-dropdown', 'options'),
     Output('sales-agent-dropdown', 'options')],
    [Input('date-range', 'start_date'),
     Input('date-range', 'end_date')]
)
def update_dropdown_options(start_date, end_date):
    if start_date is None or end_date is None:
        filtered_df = df
    else:
        filtered_df = df[(df['close_date'] >= start_date) & (df['close_date'] <= end_date)]

    return [
        [{'label': i, 'value': i} for i in filtered_df['regional_office'].unique()],
        [{'label': i, 'value': i} for i in filtered_df['sector'].unique()],
        [{'label': i, 'value': i} for i in filtered_df['product'].unique()],
        [{'label': i, 'value': i} for i in filtered_df['sales_agent'].unique()]
    ]

# Main callback for updating all charts
@app.callback(
    [Output('total-revenue', 'children'),
     Output('deals-closed', 'children'),
     Output('avg-deal-size', 'children'),
     Output('win-rate', 'children'),
     Output('revenue-over-time-chart', 'figure'),
     Output('sales-pipeline-chart', 'figure'),
     Output('top-products-chart', 'figure'),
     Output('sales-by-region-chart', 'figure'),
     Output('sales-cycle-duration-chart', 'figure'),
     Output('top-sales-agents-chart', 'figure')],
    [Input('date-range', 'start_date'),
     Input('date-range', 'end_date'),
     Input('regional-office-dropdown', 'value'),
     Input('sector-dropdown', 'value'),
     Input('product-dropdown', 'value'),
     Input('sales-agent-dropdown', 'value')]
)
def update_charts(start_date, end_date, regional_offices, sectors, products, sales_agents):
    if start_date is None:
        start_date = df['close_date'].min()
    if end_date is None:
        end_date = df['close_date'].max()

    filtered_df = df[(df['close_date'] >= start_date) & (df['close_date'] <= end_date)]

    if regional_offices:
        filtered_df = filtered_df[filtered_df['regional_office'].isin(regional_offices)]
    if sectors:
        filtered_df = filtered_df[filtered_df['sector'].isin(sectors)]
    if products:
        filtered_df = filtered_df[filtered_df['product'].isin(products)]
    if sales_agents:
        filtered_df = filtered_df[filtered_df['sales_agent'].isin(sales_agents)]

    total_revenue = filtered_df['close_value'].sum()
    deals_closed = len(filtered_df[filtered_df['deal_stage'] == 'Won'])
    avg_deal_size = filtered_df['close_value'].mean()
    win_rate = len(filtered_df[filtered_df['deal_stage'] == 'Won']) / len(filtered_df) if len(filtered_df) > 0 else 0

    revenue_over_time = px.line(filtered_df.groupby('close_date')['close_value'].sum().reset_index(), x='close_date', y='close_value', title='Revenue Over Time')

    sales_pipeline_data = filtered_df['deal_stage'].value_counts().reset_index()
    sales_pipeline_data.columns = ['deal_stage', 'count']
    sales_pipeline = px.funnel(sales_pipeline_data, x='count', y='deal_stage', title='Sales Pipeline')

    top_products = px.bar(filtered_df.groupby('product')['close_value'].sum().nlargest(5).reset_index(), x='product', y='close_value', title='Top 5 Products')
    sales_by_region = px.pie(filtered_df.groupby('regional_office')['close_value'].sum().reset_index(), values='close_value', names='regional_office', title='Sales by Region')
    sales_cycle_duration = px.histogram(filtered_df, x='sales_cycle_duration', title='Sales Cycle Duration Distribution')
    top_sales_agents = px.bar(filtered_df.groupby('sales_agent')['close_value'].sum().nlargest(10).reset_index(), x='sales_agent', y='close_value', title='Top 10 Sales Agents')

    return [
        f"${total_revenue:,.2f}",
        f"{deals_closed}",
        f"${avg_deal_size:,.2f}",
        f"{win_rate:.2%}",
        revenue_over_time,
        sales_pipeline,
        top_products,
        sales_by_region,
        sales_cycle_duration,
        top_sales_agents
    ]
