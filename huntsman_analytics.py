"""
Data Processing and Analysis Module

This module demonstrates fetching data from various web sources, processing it using Python collections, 
and writing the processed data to different file formats. It handles text, CSV, Excel, and JSON data 
and showcases skills in web scraping, data manipulation, and file I/O operations.
"""

######################
# Import Standard Libraries
######################

import csv
import pathlib
import json
from collections import Counter
import re
import logging

######################
# Import External Libraries
######################

import requests
import pandas as pd

######################
# Import Local Modules
######################

import huntsman_project_setup
import utils_huntsman

# Configure logging
logging.basicConfig(level=logging.INFO)

######################
# Function Definitions Text
######################

def fetch_and_write_txt_data(folder_name, filename, url):
    """Fetch txt data from the given URL and write it to a file."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        write_txt_file(folder_name, filename, response.text)
    except requests.exceptions.RequestException as err:
        logging.error(f"Error fetching text data: {err}")

def write_txt_file(folder_name, filename, data):
    """Write txt data to a file."""
    file_path = pathlib.Path(folder_name) / filename
    with file_path.open('w') as file:
        file.write(data)
    logging.info(f"Text data saved to {file_path}")

def process_txt_file(folder_name, filename, output_filename):
    """Process text data to generate word frequency statistics."""
    file_path = pathlib.Path(folder_name) / filename
    try:
        with file_path.open('r') as file:
            text = file.read()
            word_count = Counter(re.findall(r'\w+', text.lower()))
            with open(output_filename, 'w') as output_file:
                for word, count in word_count.items():
                    output_file.write(f"{word}: {count}\n")
        logging.info(f"Processed text data saved to {output_filename}")
    except IOError as e:
        logging.error(f"I/O error({e.errno}): {e.strerror}")

######################
# Function Definitions CSV
######################

def fetch_and_write_csv_data(folder_name, filename, url):
    """Fetch csv data from the given URL and write it to a file."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        write_csv_file(folder_name, filename, response.content.decode('utf-8'))
    except requests.exceptions.RequestException as err:
        logging.error(f"Error fetching CSV data: {err}")

def write_csv_file(folder_name, filename, data):
    """Write csv data to a file."""
    file_path = pathlib.Path(folder_name) / filename
    with file_path.open('w', newline='') as file:
        file.write(data)
    logging.info(f"CSV data saved to {file_path}")

def process_csv_file(folder_name, filename, output_filename):
    """Process CSV data to summarize row and column information."""
    file_path = pathlib.Path(folder_name) / filename
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            data = [row for row in reader]
            summary = f"Number of rows: {len(data)}\n"
            summary += f"Columns: {header}\n"
            with open(output_filename, 'w') as output_file:
                output_file.write(summary)
        logging.info(f"Processed CSV data saved to {output_filename}")
    except IOError as e:
        logging.error(f"I/O error({e.errno}): {e.strerror}")

######################
# Function Definitions Excel
######################

def fetch_and_write_excel_data(folder_name, filename, url):
    """Fetch Excel data from the given URL and write it to a file."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        write_excel_file(folder_name, filename, response.content)
    except requests.exceptions.RequestException as err:
        logging.error(f"Error fetching Excel data: {err}")

def write_excel_file(folder_name, filename, data):
    """Write excel data to a file."""
    file_path = pathlib.Path(folder_name) / filename
    with open(file_path, 'wb') as file:
        file.write(data)
    logging.info(f"Excel data saved to {file_path}")

def process_excel_file(folder_name, filename, output_filename):
    """Process Excel data to summarize statistics."""
    file_path = pathlib.Path(folder_name) / filename
    try:
        df = pd.read_excel(file_path)
        summary = f"Number of rows: {len(df)}\n"
        summary += f"Columns: {list(df.columns)}\n"
        summary += df.describe().to_string()
        with open(output_filename, 'w') as output_file:
            output_file.write(summary)
        logging.info(f"Processed Excel data saved to {output_filename}")
    except Exception as e:
        logging.error(f"Error processing Excel file: {e}")

######################
# Function Definitions Json
######################

def fetch_and_write_json_data(folder_name, filename, url):
    """Fetch JSON data from the given URL and write it to a file."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        write_json_file(folder_name, filename, response.json())
    except requests.exceptions.RequestException as err:
        logging.error(f"Error fetching JSON data: {err}")

def write_json_file(folder_name, filename, data):
    """Write JSON data to a file."""
    file_path = pathlib.Path(folder_name) / filename
    with file_path.open('w') as file:
        json.dump(data, file, indent=4)
    logging.info(f"JSON data saved to {file_path}")

def process_json_file(folder_name, filename, output_filename):
    """Process JSON data to summarize records count."""
    file_path = pathlib.Path(folder_name) / filename
    try:
        with file_path.open('r') as file:
            data = json.load(file)
            summary = f"Number of records: {len(data.get('people', []))}\n"
            with open(output_filename, 'w') as output_file:
                output_file.write(summary)
        logging.info(f"Processed JSON data saved to {output_filename}")
    except IOError as e:
        logging.error(f"I/O error({e.errno}): {e.strerror}")
    except json.JSONDecodeError as e:
        logging.error(f"JSON decode error: {e}")

######################
# Main Function
######################

def main():
    """ Main function to demonstrate module capabilities. """

    # Print byline from imported module
    print(f"Byline: {utils_huntsman.byline}")
    
    # Define the prefix for the folders
    prefix = 'data-'

    # Define the folder names for each data type
    folder_names = ['txt', 'csv', 'excel', 'json']

    # Create folders using the prefixed naming
    result = huntsman_project_setup.create_prefixed_folders(folder_names, prefix)
    print(result)

    # Define the base directory relative to the script's location
    base_dir = pathlib.Path(__file__).parent.joinpath('data')
    
    # Define URLs for data fetching
    txt_url = 'https://shakespeare.mit.edu/romeo_juliet/full.html'
    csv_url = 'https://raw.githubusercontent.com/MainakRepositor/Datasets/master/World%20Happiness%20Data/2020.csv'
    excel_url = 'https://github.com/bharathirajatut/sample-excel-dataset/raw/master/cattle.xls'
    json_url = 'http://api.open-notify.org/astros.json'

   # Define folder names 
    txt_folder_name = 'data-txt'
    csv_folder_name = 'data-csv'
    excel_folder_name = 'data-excel'
    json_folder_name = 'data-json'

    # Define filenames for data storage
    txt_filename = 'data.txt'
    csv_filename = 'data.csv'
    excel_filename = 'data.xls'
    json_filename = 'data.json'

    # Define full paths for each folder
    pathlib.Path(txt_folder_name).mkdir(parents=True, exist_ok=True)
    pathlib.Path(csv_folder_name).mkdir(parents=True, exist_ok=True)
    pathlib.Path(excel_folder_name).mkdir(parents=True, exist_ok=True)
    pathlib.Path(json_folder_name).mkdir(parents=True, exist_ok=True)

    # Fetch and write data to files
    fetch_and_write_txt_data(txt_folder_name, txt_filename, txt_url)
    fetch_and_write_csv_data(csv_folder_name, csv_filename, csv_url)
    fetch_and_write_excel_data(excel_folder_name, excel_filename, excel_url)
    fetch_and_write_json_data(json_folder_name, json_filename, json_url)

    # Process the fetched data
    process_txt_file(txt_folder_name, txt_filename, 'results_txt.txt')
    process_csv_file(csv_folder_name, csv_filename, 'results_csv.txt')
    process_excel_file(excel_folder_name, excel_filename, 'results_xls.txt')
    process_json_file(json_folder_name, json_filename, 'results_json.txt')

######################
# Conditional Execution
######################

if __name__ == '__main__':
    main()