 # TfL BikePoint Data Extractor

# This script fetches live bike station data from the Transport for London (TfL) BikePoint API.
# It performs the following tasks:

# 1. Sends a GET request to the TfL BikePoint API.
# 2. Retries the request if the response returns retryable status codes (249 or 500) up to 3 times.
# 3. Parses the JSON response and adds a timestamp to each bike station record.
# 4. Saves the data to a local JSON file named with the current timestamp.
# 5. Logs any errors during the request or data processing.


import json
import time
from datetime import datetime
import requests

# URL for the Transport for London (TfL) BikePoint API
url = 'https://api.tfl.gov.uk/BikePoint/'

def extract(url):

    # Make an initial GET request to the API with a 10-second timeout
    response = requests.get(url,timeout=10)

    # List of HTTP status codes that should trigger a retry
    retry_codes = [249,500]

    # create a retry counter and maximum number of retry attempts
    count = 0
    max_tries = 3

    # Main loop to handle retries
    while count < max_tries:
        if response.status_code == 200:
        # Successfully received a response from the API

            try:
                data = response.json() # Parse JSON content from the response
            except Exception as e:
                print(e)             #print error to show not in json format
                break
                    
            # Add a timestamp for when the data was extracted
            extract_timestamp = datetime.now()
            for bp in data:
                bp['extract_timestamp'] = str(extract_timestamp)

            # Construct a filename using the current timestamp
            filepath = 'data/' + extract_timestamp.strftime('%Y-%m-%dT%H-%M-%S') + '.json'

            # Save the processed data to a JSON file
            with open(filepath, 'w') as file:
                json.dump(data,file)
            break # Exit loop after successful processing

        elif response.status_code in retry_codes:
            # Handle retryable errors
            time.sleep(10)
            print(response.reason())
            count+=1
            # Reattempt the request
        else:
            # Handle non-retryable errors
            print(response.reason())
            break



