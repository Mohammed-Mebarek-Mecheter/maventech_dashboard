# MavenTech Sales Dashboard

This project is an interactive dashboard for MavenTech, a company that specializes in selling computer hardware. The dashboard is designed to help sales managers track their team's quarterly performance.

## Project Structure

```
maventech_dashboard/
│
├── data/
│   └── sales_data.csv
│
├── app/
│   ├── __init__.py
│   ├── data_loading.py
│   ├── layout.py
│   ├── callbacks.py
│   └── data_processing.py
│
├── assets/
│   ├── custom.css
│   └── logo.png
│
├── tests/
│   ├── test_data_loading.py
│   ├── test_layout.py
│   └── test_callbacks.py
│
├── app.py
├── requirements.txt
└── README.md
```

## Setup and Installation

1. **Clone the repository:**

```bash
git clone <repository_url>
cd maventech_dashboard
```

2. **Create a virtual environment and install the necessary packages:**

```bash
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

3. **Run the application:**

```bash
python run.py
```

4. **Access the dashboard:**

Open a web browser and navigate to `http://127.0.0.1:8050/`.

## Testing

Run the unit tests:

```bash
python -m unittest discover -s tests
```

## Features

- **Interactive Filters:** Filter data by date range, regional office, sector, product, and sales agent.
- **Key Metrics:** Display total revenue, number of deals closed, average deal size, and win rate.
- **Visualizations:**
    - Revenue Over Time
    - Sales Pipeline
    - Top Products
    - Sales by Region
    - Sales Cycle Duration
    - Top Performing Sales Agents

## Development Roadmap

1. **Project Setup and Data Loading**
2. **Dashboard Layout Design**
3. **Core Visualizations Development**
4. **Filtering and Interactivity**
5. **Advanced Visualizations and Analysis**
6. **Performance Optimization**
7. **User Experience Enhancements**
8. **Testing and Quality Assurance**
9. **Documentation and Deployment**
10. **Final Review and Launch**

## Key Considerations

1. **Efficient Data Handling:** Optimize data loading and processing for the cleaned dataset.
2. **Modularity:** Keep code modular for easy maintenance and updates.
3. **Scalability:** Design the dashboard to handle potential increases in data volume.
4. **User-Centric Design:** Prioritize intuitive navigation and clear data presentation.
5. **Performance:** Continuously monitor and optimize for fast load times and smooth interactions.
6. **Flexibility:** Build in the ability to easily add new visualizations or data sources in the future.
7. **Data Integrity:** Implement checks to ensure ongoing data quality as new data is added.
```

### 9. Requirements File

#### `requirements.txt`

```plaintext
dash==2.0.0
dash-bootstrap-components==1.0.0
pandas==1.3.3
plotly==5.3.1
```

### 10. Running the Application

Now you can run the application by executing:

```bash
python run.py
```

This setup ensures you have a well-organized project with clear separation of concerns, efficient data handling, and interactive visualizations. You can further extend the dashboard by adding more advanced visualizations and interactivity as per the development roadmap.
