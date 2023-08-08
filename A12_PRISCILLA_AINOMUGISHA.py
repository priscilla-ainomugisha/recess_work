from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv

# Function to fetch data from the API and write to the CSV file
#API  url is defined at the end of the code.
def fetch_and_write_data(api_url, csvfile):
    response = requests.get(api_url)

    print('Status code\n', response.status_code)

    #(status code 200 means success)
    if response.status_code == 200:
        data = response.json()  # Convert the response to a JSON object

        # Process the data
        num_recordings = data["numRecordings"]
        num_species = data["numSpecies"]
        page = data["page"]
        num_pages = data["numPages"]

        print(f"Total recordings found: {num_recordings}")# The number of recordings displayed coincides with those in the .csv file
        print(f"Total species found: {num_species}")
        print(f"Current page: {page}")
        print(f"Total pages: {num_pages}")

        # Process individual recording objects
        recordings = data["recordings"]

        # Create and open a CSV file in append mode
        with open(csvfile, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["Recording ID", "Species", "Country", "Locality", "Latitude", "Longitude", "Time", "Date", "URL", "Audio File URL"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Write the header row
            writer.writeheader()
            
            # Write each recording as a row in the CSV file
            for recording in recordings:
                recording_id = recording["id"]
                generic_name = recording["gen"]
                specific_name = recording["sp"]
                country = recording["cnt"]
                locality = recording["loc"]
                latitude = recording["lat"]
                longitude = recording["lng"]
                time = recording["time"]
                date = recording["date"]
                url = recording["url"]
                file_url = recording["file"]

                # Write the recording data to the CSV file
                writer.writerow({
                    "Recording ID": recording_id,
                    "Species": f"{generic_name} {specific_name}",
                    "Country": country,
                    "Locality": locality,
                    "Latitude": latitude,
                    "Longitude": longitude,
                    "Time": time,
                    "Date": date,
                    "URL": url,
                    "Audio File URL": file_url
                })

        print("Data has been successfully written to xeno_canto_recordings.csv")
    else:
        print("Failed to fetch data from the API.")

# Base API URL
base_api_url = 'https://xeno-canto.org/api/2/recordings?'#This base url returns a status code 400 unless it is queried

# Loop through the pages and fetch data, and append to the same CSV file
for page_number in range(1, 15):  # changing the page number in the query
    api_url = f'{base_api_url}query=since%3A31&page={page_number}'# query being used is from https://xeno-canto.org/explore?query=since%3A31&dir=0&order=xc&pg=1
    fetch_and_write_data(api_url, "xeno_canto_recordings.csv")
