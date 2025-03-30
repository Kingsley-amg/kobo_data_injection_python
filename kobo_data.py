# Ensure necessary packages are installed by running the following commands in your terminal:
# pip install pandas
# pip install koboextractor
# pip install python-dotenv

import pandas as pd
from koboextractor import KoboExtractor
from dotenv import load_dotenv
import os

def pull_kobo_data(api, url, form_id):
    from koboextractor import KoboExtractor
    import pandas as pd

    # Initialize KoboExtractor with the provided API and URL
    kobo = KoboExtractor(api, url, debug=False)

    # Fetch the list of assets from KoboToolbox
    assets = kobo.list_assets()
    
    # Find the UID of the asset that matches the provided form ID
    asset_uid = next((item['uid'] for item in assets['results'] if item['uid'] == form_id), None)

    # Raise an error if the form ID is not found in the assets
    if not asset_uid:
        raise ValueError(f"Form ID '{form_id}' not found in assets.")

    # Fetch the details of the asset using its UID
    asset = kobo.get_asset(asset_uid)
    
    # Retrieve the choice lists and questions associated with the asset
    choice_lists = kobo.get_choices(asset)
    questions = kobo.get_questions(asset=asset, unpack_multiples=True)

    # Fetch the raw data for the asset
    raw_data = kobo.get_data(asset_uid)
    
    # Sort the raw data by submission time
    sorted_data = kobo.sort_results_by_time(raw_data['results'])

    # Initialize an empty list to store labeled data
    labelled_data = []
    
    # Iterate through the sorted data and label each result
    for result in sorted_data:
        labelled_data.append(kobo.label_result(unlabeled_result=result, choice_lists=choice_lists, questions=questions, unpack_multiples=True))

    # Convert the labeled data into a pandas DataFrame
    labelled_data = pd.DataFrame(labelled_data)
    
    # Normalize the 'results' field in the DataFrame to flatten nested JSON structures
    labelled_data = pd.json_normalize(labelled_data['results'], errors='ignore')

    # Filter the columns to include only those with '.answer_label' in their names
    labelled_data = labelled_data[[col for col in labelled_data.columns if '.answer_label' in col]]
    
    # Rename the columns by extracting the part of the name between '/' and '.answer_label'
    labelled_data.columns = [col.split('/')[1].split('.answer_label')[0] if '.answer_label' in col else col for col in labelled_data.columns]

    # Return the processed and labeled data as a DataFrame
    return labelled_data

# Call the function to pull and process data from KoboToolbox
# labelled_data = pull_kobo_data(api, url, form_id)

# # Display the processed data
# labelled_data
