import requests
import logging

# Configure the logging format
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def fetch_user_data(user_id):
    url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    logging.info(f"Initiating GET request to {url}")
    
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        
        # Log successful operations
        logging.info(f"Request successful. Status Code: {response.status_code}")
        
        user_data = response.json()
        logging.info(f"Data retrieved for user: {user_data.get('name')}")
        return user_data
        
    except requests.exceptions.HTTPError as http_err:
        # Log errors with the ERROR level
        logging.error(f"HTTP error occurred: {http_err}")
    except requests.exceptions.Timeout as timeout_err:
        logging.error(f"Request timed out: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        logging.error(f"General request error: {req_err}")

# Test the logged function
fetch_user_data(1)