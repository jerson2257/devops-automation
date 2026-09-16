import requests

def post_and_verify():
    url = 'https://jsonplaceholder.typicode.com/posts'
    new_data = {
        "title": "Verification Test",
        "body": "Ensuring the payload matches",
        "userId": 99
    }
    
    # Step 1: Create the data (POST)
    print("Sending POST request...")
    response = requests.post(url, json=new_data, headers={'Content-Type': 'application/json'})
    
    if response.status_code == 201:
        server_response = response.json()
        print(f"Record successfully created with server-assigned ID: {server_response.get('id')}")
        
        # Step 2: Verify the data
        print("Verifying data integrity...")
        if server_response['title'] == new_data['title'] and server_response['body'] == new_data['body']:
            print("Verification Passed: The server returned the exact data we submitted.")
        else:
            print("Verification Failed: The returned data does not match our payload.")
    else:
        print(f"Creation failed with status: {response.status_code}")

post_and_verify()