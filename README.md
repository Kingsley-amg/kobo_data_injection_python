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
