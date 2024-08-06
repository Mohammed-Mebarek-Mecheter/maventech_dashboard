# MavenTech Sales Data Exploratory Data Analysis Report

## 1. Dataset Overview

The dataset contains 7,375 entries with 18 columns, covering various aspects of B2B sales opportunities for MavenTech, a company specializing in computer hardware sales. The data includes information on sales agents, products, accounts, deal stages, and financial metrics.

### Key Dataset Characteristics:
- No missing values in any columns
- Mix of categorical and numerical data types
- Date range: The exact range isn't clear from the provided EDA, but we see data from at least 2016 to 2017

## 2. Data Distribution and Summary Statistics

### 2.1 Numerical Variables

Key numerical variables include:
- close_value
- sales_price
- year_established
- revenue
- employees

The `describe()` function was used to generate summary statistics, but specific values weren't provided in the EDA code. However, we can infer:

- There's likely a wide range in `close_value` and `sales_price`, given the use of histograms with 50 bins
- `year_established` ranges from at least 1988 to 2012, based on the sample data shown

### 2.2 Categorical Variables

Key categorical variables include:
- deal_stage
- regional_office
- sector
- product
- sales_agent

Notable observations:
- There are 30 unique sales agents
- 7 unique products
- 85 unique accounts
- 4 deal stages
- 3 regional offices
- 10 sectors
- 15 office locations
- 8 parent companies (subsidiary_of)
- 4 product series

Most frequent categories:
- deal_stage: "Won" (4,238 occurrences)
- regional_office: "Central" (2,901 occurrences)
- sector: "retail" (1,397 occurrences)
- office_location: "United States" (6,120 occurrences)
- subsidiary_of: "Independent" (6,083 occurrences)
- series: "GTX" (3,545 occurrences)

## 3. Key Visualizations and Insights

### 3.1 Distribution of Close Value and Sales Price

Two histograms were created to visualize the distribution of `close_value` and `sales_price`. Without seeing the actual plots, we can infer:
- Both distributions are likely right-skewed, which is common in sales data
- There may be outliers on the high end of both variables
- The majority of deals probably cluster around lower values

### 3.2 Deal Stages

A count plot of deal stages shows:
- "Won" deals are the most frequent (4,238)
- The exact counts for other stages aren't provided, but we can infer that "Lost" deals are less common

### 3.3 Regional Office Performance

A count plot of regional offices reveals:
- The Central office handles the most deals (2,901)
- There are two other offices, but their deal counts aren't specified

### 3.4 Sector Analysis

A count plot of sectors indicates:
- Retail is the most represented sector (1,397 deals)
- There are 9 other sectors, but their specific counts aren't provided

### 3.5 Temporal Analysis

Two bar plots were created to show monthly trends:
- Monthly count of deals closed
- Monthly revenue from closed deals

Without seeing the actual plots, we can't provide specific insights, but these visualizations would reveal any seasonality or trends in deal closure and revenue generation.

### 3.6 Correlation Analysis

A correlation matrix heatmap was generated for numerical variables. While specific correlations aren't provided, this visualization would highlight any strong relationships between variables like `close_value`, `sales_price`, `revenue`, and `employees`.

## 4. Areas for Further Investigation

Based on the EDA, several areas warrant deeper analysis in the dashboard:

1. **Sales Performance Metrics**:
    - Track total revenue, number of deals closed, and average deal size over time
    - Analyze conversion rates from 'Engaging' to 'Won' stages

2. **Regional Performance**:
    - Compare the performance of the three regional offices
    - Investigate why the Central office handles more deals and if this translates to higher revenue

3. **Sector Analysis**:
    - Explore which sectors are most profitable
    - Identify any sectors with high potential but low current performance

4. **Product Performance**:
    - Analyze which products and series are best-selling
    - Investigate the relationship between sales price and close value

5. **Sales Agent Performance**:
    - Compare performance metrics across sales agents
    - Identify top performers and their strategies

6. **Temporal Trends**:
    - Analyze quarterly and monthly trends in sales and revenue
    - Identify any seasonality or cyclical patterns

7. **Deal Size vs. Company Size**:
    - Investigate if there's a correlation between deal size and client company size (revenue, employees)

8. **Sales Cycle Duration**:
    - Calculate and analyze the time between engage_date and close_date
    - Identify factors that might influence sales cycle length

## 5. Recommendations for Dashboard Development

1. Include filters for key dimensions: sales agent, regional office, sector, and product
2. Create time-based visualizations to track performance over months and quarters
3. Develop comparative views to benchmark performance across different categories
4. Include distribution plots for key metrics to identify outliers and general trends
5. Create a correlation view to help users understand relationships between numerical variables
6. Implement drill-down capabilities to move from high-level overviews to detailed individual deal information

By focusing on these areas, the dashboard will provide sales managers with comprehensive insights into their team's quarterly performance and help drive data-informed decision-making at MavenTech.
