import pandas as pd
import re
import os
import shutil
import logging
from typing import Dict, Optional, Callable, Any

# --- Step 1: Configure Logging ---
# Sets up a logger that provides informative output with timestamps.
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# --- Step 2: Centralized Data Configuration ---
# This dictionary drives the entire script. To add a new data source,
# you only need to add a new entry here.
DATA_CONFIG = {
    "all_arms_imports": {
        "path": "sipri/TIV-Import-All-1950-2022.csv",
        "loader_options": {"index_col": "Arms Category"},
        "cleaner_func": None
    },
    "all_arms_exports": {
        "path": "sipri/TIV-Export-All-1950-2022.csv",
        "loader_options": {"index_col": "Arms Category"},
        "cleaner_func": None
    },
    "top_200_arms_imports": {
        "path": "sipri/TIV-Import-Top-200-1950-2022.csv",
        "loader_options": {"index_col": "Rank 1950-2022"},
        "cleaner_func": None
    },
    "top_200_arms_exports": {
        "path": "sipri/TIV-Export-Top-200-1950-2022.csv",
        "loader_options": {"index_col": "Rank 1950-2022"},
        "cleaner_func": None
    },
    "bloomberg_defense_industry": {
        "path": "bloomberg/BI_AEROG_1 Defense Industry.csv",
        "loader_options": {"index_col": "Description"},
        "cleaner_func": None
    },
    "bloomberg_us_can_construction": {
        "path": "bloomberg/BI_CONSG_1 DATA US CAN.csv",
        "loader_options": {"index_col": "Description"},
        "cleaner_func": None
    },
    "bloomberg_defense_budget": {
        "path": "bloomberg/BI_DEFCG_1Defense Budget.csv",
        "loader_options": {"index_col": "Description"},
        "cleaner_func": None
    },
    "bloomberg_cybersecurity_fundflows": {
        "path": "bloomberg/BI_ETFSG_1 Sector keyword cybersecurity fundflows equity.csv",
        "loader_options": {"index_col": "Description"},
        "cleaner_func": None
    },
    "gdp": {
        "path": "world_bank/GDP_1960-2022.csv",
        "loader_options": {}, # No index column for this file initially
        "cleaner_func": lambda df: clean_gdp_headers(df) # Use a lambda for the specific cleaner
    }
}

# --- Step 3: Path Helper Functions ---
def get_data_path(relative_path: str, base_folder: str = 'raw') -> str:
    """
    Constructs the absolute path to a data file.
    Args:
        relative_path: The path of the file relative to the 'data/raw' or 'data/processed' folder.
        base_folder: The base folder, either 'raw' or 'processed'.
    Returns:
        The absolute path to the data file.
    """
    base_path = os.path.join(os.path.dirname(__file__), '..', 'data')
    return os.path.join(base_path, base_folder, relative_path)

# --- Step 4: Data Cleaning & Transformation Functions ---
def fill_na_values(df: pd.DataFrame) -> pd.DataFrame:
    """Fills NA values with 0. A generic cleaning step."""
    return df.fillna(0)

def clean_gdp_headers(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the column headers of the GDP dataframe.
    This function removes the bracketed year information from the column headers.
    For example, '1960 [YR1960]' becomes '1960'.
    """
    logging.info("Cleaning GDP headers...")
    # This pattern matches a space, opening bracket, any characters, and a closing bracket.
    pattern = r' \[\w*\]'
    # Using a dictionary for renaming is efficient
    new_columns = {col: re.sub(pattern, '', col) for col in df.columns}
    df = df.rename(columns=new_columns)
    logging.info("GDP headers cleaned successfully.")
    return df

# --- Step 5: Main Orchestration Logic ---
def preprocess_all_data():
    """
    Orchestrates the entire data preprocessing pipeline:
    1. Cleans the processed data directory.
    2. Loads raw data based on the DATA_CONFIG.
    3. Applies generic and specific cleaning functions.
    4. Saves the processed dataframes to the 'data/processed' directory.
    """
    processed_dir = os.path.join(os.path.dirname(__file__), '..', 'data', 'processed')

    # Start with a clean slate
    if os.path.exists(processed_dir):
        logging.info(f"Removing existing processed data directory: {processed_dir}")
        shutil.rmtree(processed_dir)
    logging.info(f"Creating empty processed data directory: {processed_dir}")
    os.makedirs(processed_dir)

    processed_data = {}
    for name, config in DATA_CONFIG.items():
        try:
            raw_file_path = get_data_path(config['path'], base_folder='raw')
            logging.info(f"Processing dataset: '{name}' from '{raw_file_path}'")
            
            # Load data with specified options
            df = pd.read_csv(raw_file_path, **config['loader_options'])

            # Apply generic cleaning steps
            df = fill_na_values(df)

            # Apply dataset-specific cleaning function if one is defined
            cleaner_func = config.get('cleaner_func')
            if cleaner_func:
                df = cleaner_func(df)

            # Store and save the processed dataframe
            processed_data[name] = df
            output_path = get_data_path(f"{name}.csv", base_folder='processed')
            df.to_csv(output_path)
            logging.info(f"Successfully saved processed data to '{output_path}'")

        except FileNotFoundError:
            logging.error(f"File not found for dataset '{name}': {raw_file_path}. Skipping.")
        except Exception as e:
            logging.error(f"An error occurred while processing dataset '{name}': {e}. Skipping.")

    # Placeholder for a future merging step
    # merge_data(processed_data)

# --- Step 6: Script Execution ---
if __name__ == '__main__':
    logging.info("===== Starting Data Preprocessing Pipeline =====")
    preprocess_all_data()
    logging.info("===== Data Preprocessing Pipeline Finished Successfully =====")