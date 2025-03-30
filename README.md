# KoboToolbox Data Extraction and Processing

This repository contains a Python script for extracting, processing, and labeling survey data from KoboToolbox using the `KoboExtractor` library. The script retrieves survey data, normalizes nested JSON structures, and formats the results into a clean pandas DataFrame for further analysis.

---

## 📚 Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [Parameters](#parameters)
- [Returns](#returns)
- [Example Usage](#example-usage)
- [Output](#output)
- [Error Handling](#error-handling)

---

## ✅ Features

- Connects to KoboToolbox using an API key and base URL.
- Fetches survey assets and their associated data.
- Labels raw survey data using choice lists and questions metadata.
- Normalizes nested JSON structures into a flat pandas DataFrame.
- Filters and renames columns for easier analysis.

---

## 🛠 Requirements

Ensure the following Python packages are installed:

- `pandas`
- `koboextractor`
- `python-dotenv`

---

## ⬇️ Installation

Install the required packages using pip:

```bash
pip install pandas koboextractor python-dotenv

---

Environment Setup 🔐 
Create a .env file in the root directory of your project to store sensitive credentials:

api=your_api_key
url=https://your_base_url
form_id=your_form_id

api: Your KoboToolbox API key.
url: The base URL of your KoboToolbox instance (https://kf.kobotoolbox.org or https://eu.kobotoolbox.org).
form_id: The unique ID of the form you want to process.


Usage Guide ▶️

Parameters ⚙️
api (str): The API key for authentication.
url (str): The base URL of the KoboToolbox instance.
form_id (str): The unique ID of the form to process.

Returns 📤
A pandas.DataFrame containing the processed and labeled survey data.

Example Usage 🧪

from kobo_data import pull_kobo_data
import os

# Load environment variables
api = os.getenv('api')
url = os.getenv('url')
form_id = os.getenv('form_id')

# Call the function to pull and process data
try:
    labelled_data = pull_kobo_data(api, url, form_id)
    print(labelled_data.head())  # Display the first few rows
except Exception as e:
    print(f"An error occurred: {e}")


Output 📊
The function returns a pandas DataFrame with the following characteristics:
Flattened JSON data from the survey results.
Columns filtered to include only those with .answer_label in their names.
Columns renamed for clarity by extracting meaningful parts of their names.

Error Handling 🧯

The script includes error handling for:
Missing or invalid form IDs.
Empty or malformed responses from the KoboToolbox API.
Missing or undefined environment variables.
