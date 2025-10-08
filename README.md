# Sleep Health Analysis

This project investigates the relationship between **sleep patterns,
cardiovascular health, and lifestyle factors**. It combines data
cleaning scripts, reusable functions, and exploratory notebooks to
support hypothesis testing and potential app development.

## Business Objective

Original concept: prototype a health app that leverages wearable/device
data to help users increase daily activity, thereby improving sleep
duration and overall health.

-   **H₀:** No relationship between sleep duration (X) and physical
    activity duration (y).
-   **Focus areas:** Sleep disorders, BMI, cardiovascular data, and
    blood pressure.

------------------------------------------------------------------------

## Repository Structure

    sleep-health-analysis/
    ├── main.ipynb         # Exploratory notebook (EDA, hypothesis testing, regressions)
    ├── cleaning.py        # Data cleaning and preprocessing functions
    ├── functions.py       # Helper functions (blood pressure parsing, categorization)
    ├── data/              # Place raw/interim/processed data here
    ├── README.md          # Project overview (this file)
    └── .gitignore

------------------------------------------------------------------------

## Key Components

### 1. `main.ipynb`

-   Loads and inspects raw data
    (`Sleep_health_and_lifestyle_dataset.csv`).
-   Cleans data using `cleaning.py`.
-   Exploratory Data Analysis:
    -   Histograms of numeric features
    -   Sleep duration statistics
    -   Correlation analysis (Pearson's r, regression)
-   Hypothesis testing on activity vs. sleep.

### 2. `cleaning.py`

Contains modular functions for data cleaning: - `clean_sleep_disorder`
-- fills missing values in *Sleep Disorder* column.
- `lowercase_columns` -- standardizes column names to lowercase.
- `add_underscore` -- replaces spaces with underscores in column names.
- `rename_columns` -- renames columns for clarity.
- `remove_duplicates` -- drops duplicate rows.
- `standardize_bmi_category` -- normalizes BMI labels.
- `rename_cvd_columns`, `clean_cvd_data` -- preprocess cardiovascular
dataset.
- `rename_wiki_columns`, `drop_wiki_columns`, `clean_wiki_data` -- clean
wiki-based health datasets.
- `drop_na`, `level_columns`, `get_table` -- general cleaning
utilities.
- `clean_data` -- master function that applies multiple steps in
sequence.

### 3. `functions.py`

Utility functions for cardiovascular metrics: - `create_bp_columns(df)`
→ splits `"blood_pressure"` into `systolic` and `diastolic` columns.
- `bp_category(row)` → categorizes blood pressure into Normal / Elevated
/ High / Hypertensive Crisis.

------------------------------------------------------------------------

## Usage

1.  **Clone and install**

    ``` bash
    git clone https://github.com/chandlershortlidge/sleep-health-analysis.git
    cd sleep-health-analysis
    python -m venv venv
    source venv/bin/activate  # or venv\Scripts\activate on Windows
    pip install -r requirements.txt
    ```

2.  **Prepare data**

    -   Place raw datasets in `data/raw/`.
    -   Example: `data/raw/Sleep_health_and_lifestyle_dataset.csv`.

3.  **Run analysis**

    -   Open `main.ipynb` in Jupyter and run all cells.

    -   Or import functions in Python:

        ``` python
        import pandas as pd
        import cleaning as cl
        import functions as fn

        df = pd.read_csv("data/raw/Sleep_health_and_lifestyle_dataset.csv")
        df = cl.clean_data(df)
        df = fn.create_bp_columns(df)
        df["bp_category"] = df.apply(fn.bp_category, axis=1)
        ```

------------------------------------------------------------------------

## Next Steps

-   Package cleaning + analysis into a reproducible `pipeline.py`.
-   Add visualization utilities (`viz.py`) for automated report
    generation.
-   Write unit tests for cleaning functions.
-   Create a lightweight CLI for one-command analysis.

------------------------------------------------------------------------

## License

MIT License --- free to use and adapt.
