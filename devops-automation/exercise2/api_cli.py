import requests

def api_cli():
    base_url = 'https://jsonplaceholder.typicode.com/posts'
    
    while True:
        print("\n--- API CLI Tool ---")
        print("1. Get a specific post (Read)")
        print("2. Create a new post (Create)")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            post_id = input("Enter the Post ID (e.g., 1): ")
            response = requests.get(f"{base_url}/{post_id}", timeout=5)
            
            if response.status_code == 200:
                post = response.json()
                print(f"\nTitle: {post['title']}\nBody: {post['body']}")
            else:
                print(f"\nFailed! Status Code: {response.status_code}")
                
        elif choice == '2':
            title = input("Enter new post title: ")
            body = input("Enter new post body: ")
            new_post = {"title": title, "body": body, "userId": 1}
            
            response = requests.post(base_url, json=new_post, headers={'Content-Type': 'application/json'})
            if response.status_code == 201:
                print(f"\nSuccess! New post created with ID: {response.json()['id']}")
            else:
                print("\nFailed to create post.")
                
        elif choice == '3':
            print("Exiting tool...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    api_cli()