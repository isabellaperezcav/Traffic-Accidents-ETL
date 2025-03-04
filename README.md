
# Traffic-Accidents-ETL

## General Description

This project implements an **Extract, Transform, Load (ETL)** pipeline to process and analyze traffic accident data. Its purpose is to demonstrate advanced skills in data management, transformation, and visualization by migrating a dataset from a CSV file to a PostgreSQL database, performing an exploratory data analysis (EDA), and creating interactive visualizations with Power BI.

### Objectives
- Extract data from a CSV file obtained from Kaggle.
- Transform the data through cleaning, feature engineering, and standardization.
- Load the transformed data into a PostgreSQL database.
- Perform an exploratory data analysis (EDA) to identify patterns and trends.
- Visualize the results in an interactive Power BI dashboard.

---

## Data Source

The dataset comes from **[Kaggle: Traffic Accidents](https://www.kaggle.com/datasets/oktayrdeki/traffic-accidents)**. It contains over 10,000 records and multiple features related to traffic accidents, such as accident severity, weather conditions, and temporal data. The raw data is migrated to a PostgreSQL database for processing and analysis.

---

## ETL Pipeline

### Extraction
- **Source**: The data is extracted from the `traffic_accidents.csv` file.
- **Method**: The CSV file is read into a Pandas DataFrame using Python.

### Transformation
The following transformations are applied to clean and prepare the data:
- **Data Cleaning**:
  - Removal of null values and duplicates.
  - Replacement of `"UNKNOWN"` values with `"OTHER"` in categorical columns such as `weather_condition` and `road_defect`.
- **Feature Engineering**:
  - Conversion of `crash_date` to datetime format for temporal analysis.
  - Transformation of `most_severe_injury` into an ordered categorical variable with levels:
    - `NO INDICATION OF INJURY`
    - `REPORTED, NOT EVIDENT`
    - `NON-INCAPACITATING INJURY`
    - `INCAPACITATING INJURY`
    - `FATAL`
  - Conversion of `intersection_related` to a binary indicator (1 for `'Y'`, 0 otherwise).
- **Standardization**: Ensuring consistency in categorical columns.

These transformations are performed in a Jupyter Notebook (`002_EDA.ipynb`) and validated before loading.

### Loading
- **Destination**: The transformed data is stored in the `accidentes_limpios` table of a PostgreSQL database.
- **Method**: The cleaned DataFrame is written to the database using SQLAlchemy's `to_sql` method.

---

## Exploratory Data Analysis (EDA)

EDA is performed in `002_EDA.ipynb` using data from the PostgreSQL database. The main activities include:
- **Data Summary**: Inspection of column types, counts of non-null values, and descriptive statistics.
- **Univariate Analysis**: Distribution of variables such as `weather_condition` and `most_severe_injury`.
- **Bivariate Analysis**: Relationships between variables, such as `weather_condition` vs. `injuries_total`.
- **Temporal Analysis**: Trends by `crash_hour`, `crash_day_of_week`, and `crash_month`.

The EDA provides the foundation for visualizations and key insights.

---

## Visualizations

An **interactive Power BI dashboard** (`proyectoETL.pbix`) includes the following visualizations:
- **Total Accidents by Severity**: Bar chart of accidents by `most_severe_injury`.
- **Accidents by Conditions**: Comparison of accidents based on `weather_condition` and `lighting_condition`.
- **Temporal Trends**: Visualizations of accidents by hour, day, and month.
- **Road and Traffic Factors**: Analysis by `traffic_control_device`, `road_defect`, and `trafficway_type`.

The dashboard offers filters for interactive exploration.

---

## Project Structure

```
📂 Traffic-Accidents-ETL
│── 📂 config          # Configuration files (e.g., database connection)
│   ├── requirements.txt   # Project dependencies
│   ├── conexion_db.py   # PostgreSQL database connection script
│── 📂 data            # Input data
│   ├── traffic_accidents.csv # Original Kaggle dataset
│── 📂 notebooks       # Notebooks for EDA and transformations
│   ├── 001_extract.ipynb  # Data loading from CSV to DB and table creation
│   ├── 002_EDA.ipynb  # Exploratory data analysis
│── 📂 Dashboard       # Power BI files
│   ├── proyectoETL.pbix  # Interactive dashboard
│   ├── proyectoETL.pdf   # Dashboard in PDF format
│── .gitignore         # Files to ignore in Git
│── README.md          # Project documentation
```

---

## Technologies Used

- **Programming**: Python  
- **Data Manipulation**: pandas, numpy  
- **Visualization**: matplotlib, seaborn, Power BI Desktop  
- **Database**: PostgreSQL, psycopg2, SQLAlchemy  
- **Environment**: Jupyter Notebook  
- **Version Control**: Git, GitHub  

---

## Final Data Destination

- **Database**: The cleaned data is stored in the `accidentes_limpios` table in PostgreSQL.
- **Dashboard**: Visualized in `proyectoETL.pbix` for interactive insights.

---

## Performance and Findings

- **Efficiency**: The ETL pipeline handles large datasets (>10k rows) with optimized operations in Python and SQL.
- **Key Findings**:
  - Adverse weather and lighting conditions correlate with a higher number of injuries.
  - Peak accident times (e.g., rush hours) and days (e.g., weekends) were identified.
  - Most accidents do not show evident injuries, but severe cases require more attention.

---

## Project Requirement Alignment

This project meets the requirements of the "ETL Project - First Delivery":
- **Dataset**: Over 10,000 rows from Kaggle.
- **ETL**: CSV migration to a database, transformation, and data loading.
- **EDA**: Conducted in Jupyter Notebook using database data.
- **Visualizations**: Generated from the database in Power BI.
- **Technologies**: Use of Python, Jupyter, PostgreSQL, Power BI, and GitHub.

---

### Installation

To set up this project on your local machine, follow these steps:

1. **Clone the repository**:
    
    ```bash
    git clone <https://github.com/isabellaperezcav/Traffic-Accidents-ETL.git>
    cd Traffic-Accidents-ETL
    ```
    
2. **Create and activate a virtual environment**:
    
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\\Scripts\\activate
    ```
    
3. **Install dependencies**:
    
    ```bash
    pip install -r requirements.txt
    ```
    
4. **Set up the PostgreSQL database**:
    - Ensure PostgreSQL is installed and running.
    - Create a database for the project:
        
        ```sql
        CREATE DATABASE traffic_accidents_db;
        ```
        
    - Update the connection credentials in the configuration file (you need to create the `.env` file).

5. **Run the database connection script**:
    
    ```bash
    python config.conexion_db.py
    ```
    
6. **Run the notebooks**:
    - Ensure the PostgreSQL database connection is correctly set up.
    - Open `001_extract.ipynb` and run the cells to migrate the CSV to the database.
    - Open `002_EDA.ipynb` and run the cells to explore and clean the data.

7. **Set up Power BI or view the charts from the PDF**:
    - Open `proyectoETL.pbix` in Power BI Desktop.
    - Ensure the PostgreSQL database connection is correctly configured.

---

## Conclusion

The "Traffic-Accidents-ETL" project demonstrates a complete data pipeline, from extraction and transformation to analysis and visualization. By processing the Kaggle traffic accident dataset and creating an interactive dashboard, the project provides actionable insights into accident patterns, supporting data-driven strategies for road safety.

---