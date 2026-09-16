import requests
import time
from requests.exceptions import RequestException

def fetch_with_retry(url, max_retries=3, delay_seconds=2):
    """Fetches data from an API and retries if a network error occurs."""
    
    for attempt in range(max_retries):
        try:
            print(f"Attempt {attempt + 1} of {max_retries}...")
            # Using the 5-second timeout as recommended in the midterm prep
            response = requests.get(url, timeout=5)
            response.raise_for_status() # Raises an exception for 4xx/5xx status codes
            
            print("Success!")
            return response.json()
            
        except RequestException as req_err:
            print(f"Error encountered: {req_err}")
            
            # If this wasn't our last attempt, wait before trying again
            if attempt < max_retries - 1:
                print(f"Retrying in {delay_seconds} seconds...\n")
                time.sleep(delay_seconds)
            else:
                print("Max retries reached. Request failed.")
                return None

# Test the function
result = fetch_with_retry('https://jsonplaceholder.typicode.com/posts/1')
if result:
    print(f"Fetched Data: {result['title']}")