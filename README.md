TfL BikePoint Data Extractor

This script fetches live bike station data from the Transport for London (TfL) BikePoint API.
It performs the following tasks:

1. Sends a GET request to the TfL BikePoint API.
2. Retries the request if the response returns retryable status codes (249 or 500) up to 3 times.
3. Parses the JSON response and adds a timestamp to each bike station record.
4. Saves the data to a local JSON file named with the current timestamp.
5. Logs any errors during the request or data processing.