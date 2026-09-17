
# Duplicate Detection & Data Quality Analytics Engine

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![License](https://img.shields.io/badge/License-MIT-green)

## Project Overview

The **Duplicate Detection & Data Quality Analytics Engine** is a Python-based data analytics project that identifies duplicate records, evaluates data quality, and compares the performance of different duplicate detection algorithms.

The project combines **Data Structures and Algorithms (DSA), Python, data preprocessing, algorithmic complexity analysis, and business-oriented data quality reporting**.

## Objectives

- Identify duplicate records in datasets.
- Detect duplicate keys and repeated customer information.
- Handle missing values and inconsistent data.
- Calculate data quality scores.
- Compare algorithm performance.
- Generate analytical reports.
- Provide an interactive Streamlit dashboard.

## Key Features

- Data ingestion and preprocessing
- Missing-value analysis
- Duplicate record detection
- Duplicate-key analysis
- Data quality scoring
- Algorithm benchmarking
- Statistical summaries
- Interactive dashboard
- Automated testing

## Duplicate Detection Algorithms

| Algorithm | Purpose | Average Complexity |
|---|---|---|
| Brute Force | Compares records directly | O(n²) |
| Sorting-Based | Sorts values and checks neighbors | O(n log n) |
| Hash Set | Uses a set to identify duplicates | O(n) |
| Frequency Map | Counts repeated values | O(n) |

*Complexities are typical estimates and may vary based on implementation and data characteristics.*

## Technology Stack

- **Programming:** Python
- **Data Analysis:** Pandas, NumPy
- **Visualization:** Matplotlib
- **Dashboard:** Streamlit
- **Testing:** Pytest
- **Development:** VS Code
- **Version Control:** Git and GitHub

## Project Structure

```text
duplicate-detection-data-quality-engine/
│
├── README.md
├── LICENSE
├── requirements.txt
├── pyproject.toml
│
├── src/
│   └── duplicate_engine/
│       ├── algorithms/
│       ├── analytics/
│       ├── ingestion/
│       ├── preprocessing/
│       └── reports/
│
├── tests/
├── data/
├── reports/
├── streamlit/
└── run_cleaning.py
```

## Installation

Clone the repository:

```bash
git clone https://github.com/smahammedsahil922-cloud/duplicate-detection-data-quality-engine.git
```

Navigate to the project:

```bash
cd duplicate-detection-data-quality-engine
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the data cleaning pipeline:

```bash
python run_cleaning.py
```

Run tests:

```bash
python -m pytest
```

Launch the Streamlit dashboard:

```bash
streamlit run streamlit/app.py
```

## Data Quality Metrics

The project can analyze:

- Total number of records
- Unique records
- Duplicate records
- Duplicate percentage
- Missing-value percentage
- Duplicate-key frequency
- Overall data quality indicators

## Learning Outcomes

This project demonstrates practical knowledge of:

- Data Structures and Algorithms
- Python programming
- Data cleaning and preprocessing
- Data quality analytics
- Algorithmic time complexity
- Software project organization
- Testing and documentation
- Dashboard development

## Future Improvements

- Fuzzy matching for similar records
- Machine learning-based entity resolution
- Database integration with MySQL
- Advanced benchmarking visualizations
- Automated data quality reports
- Cloud deployment

## Author

**S Mohammed Sahil**

M.Sc. Economics and Data Analytics  
Central University of Andhra Pradesh

### Areas of Interest

- Data Analytics
- Business Intelligence
- Machine Learning
- Data Quality Engineering
- Economic Research

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
