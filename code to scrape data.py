from dotenv import load_dotenv
import os
import pandas as pd
from serpapi import GoogleSearch

# Load environment variables from .env file
load_dotenv(dotenv_path="path to your .env file that you can get from the serpAPI website and store in your workspace")

# Get the SERP_API_KEY from the environment
serp_api_key = os.getenv("SERP_API_KEY")

# Confirm the API key is loaded
if serp_api_key is None:
    raise ValueError("API Key not found. Check your .env file.")

#initialize a list to store all the scraped data in
results_list = []
page_number = 0
next_link = None

#You can find this on the SerpAPI website
while True:
    params = {
        'engine': 'google_maps',
        'q': 'restaurants',#whatever you want to be in the searchbar of google maps (hotels, gas stations etc.)
        'll': 'enter latitude longitude and zoom here in the format @latitude,longitude,zoom',  
        'type': 'search',
        'api_key': serp_api_key
    }

    # Custom logic to scrape as many results as possible
    # If we're paginating, include the next link's start value
    if next_link:
        params['start'] = next_link.split("start=")[1].split("&")[0]

    try:
        search = GoogleSearch(params)
        response = search.get_dict()  # Store the full response


        # Save the results
        results_list.append({
            'page_number': page_number,
            'data': response
        })

        # Check if there is a next page
        serpapi_pagination = response.get("serpapi_pagination", {})
        next_link = serpapi_pagination.get("next")

        # Break the loop if there is no next link (last page)
        if not next_link:
            break

        # Increment the page number
        page_number += 1

    except Exception as e:
        print(f"An error occurred on page {page_number}: {e}")
        break
    
    # Last element is *usually* empty, so we get rid of it
    # Check if the last element contains the 'search_information' with valid restaurant data
if 'search_information' in results_list[-1]['data']:
    search_info = results_list[-1]['data']['search_information']
    
    # If the 'local_results_state' indicates empty, pop the last element
    if search_info.get('local_results_state') == 'Fully empty':
        results_list.pop()
else:
    # If there's no 'search_information' at all, also pop the last element
    results_list.pop()

# Let us extract meaning full data from the results_list
all_restaurants = []

for page in results_list:
    # Check if 'local_results' exists in the page data
    if 'local_results' in page['data']:
        # Add all restaurants from this page to the combined list
        all_restaurants.extend(page['data']['local_results'])
        
# Assuming 'all_restaurants' contains all the restaurant data across pages
# If you want to assign index to each restaurant
index_counter = 1  # Start index from 1

# Loop through each restaurant and add an 'index' key
for restaurant in all_restaurants:
    restaurant['index'] = index_counter
    index_counter += 1  # Increment the index for each restaurant

# Check for all possible unique key values across all restaurant entries
list_keys = []
for each in all_restaurants[:5]:
    for k,v in each.items():
        list_keys.append(k) 
print(list(set(list_keys)))       

# Filter out the keys you want as columns in your dataframe
keys_to_retain = ['index','title','rating','reviews','type','address','phone','website','gps_coordinates','service_options']

# Only keep the K,V pair if the key is desired, else pop the dictionary
for each in all_restaurants:
    keys_to_remove = [key for key in each if key not in keys_to_retain]
    for key in keys_to_remove:
        del each[key]

# New list that doesn't have nested dictionary keys
# Easier to make a Dataframe
flattened_data = []
for idx, restaurant in enumerate(all_restaurants):
    # Create a new dictionary for each restaurant
    flat_restaurant = {}

    # Add the index field first
    flat_restaurant['index'] = restaurant.get('index', idx + 1)  # Use idx as a fallback index
    flat_restaurant['title'] = restaurant.get('title')
    flat_restaurant['rating'] = restaurant.get('rating')
    flat_restaurant['reviews'] = restaurant.get('reviews')
    flat_restaurant['type'] = restaurant.get('type')
    flat_restaurant['address'] = restaurant.get('address')
    flat_restaurant['phone'] = restaurant.get('phone')
    flat_restaurant['website'] = restaurant.get('website')

    # Extract latitude and longitude from gps_coordinates
    if 'gps_coordinates' in restaurant:
        flat_restaurant['latitude'] = restaurant['gps_coordinates'].get('latitude')
        flat_restaurant['longitude'] = restaurant['gps_coordinates'].get('longitude')
    
    # Extract service options as separate columns
    if 'service_options' in restaurant:
        flat_restaurant['dine_in'] = restaurant['service_options'].get('dine_in', False)
        flat_restaurant['drive_through'] = restaurant['service_options'].get('drive_through', False)
        flat_restaurant['no_contact_delivery'] = restaurant['service_options'].get('no_contact_delivery', False)

    # Append the flattened restaurant data to the list
    flattened_data.append(flat_restaurant)

# Create a Dataframe from the cleaned list of data
df = pd.DataFrame(flattened_data)
# Save it to CSV format (Optional)
df.to_csv('file_name.csv')