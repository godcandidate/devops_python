import requests

# The API endpoint
post_url = "https://jsonplaceholder.typicode.com/posts"
get_url = "https://jsonplaceholder.typicode.com/posts/12"

def send_data(url):
    """
    Sends data to the API using a POST request.
    """
    data = {
        "userID": 12,
        "title": "Making a POST request",
        "body": "This is the data we created."
    }

    response = requests.post(url, json=data)

    # Print the response
    if response.status_code == 201:  # 201 indicates successful resource creation
        print("Data sent successfully!")
    else:
        print("Failed to send data.")
    
    print("Response:", response.json())


def get_data(url):
    """
    Retrieves data from the API using a GET request.
    """
    response = requests.get(url)

    # Print the response
    if response.status_code == 200:
        print("Data retrieved successfully!")
        print("Response:", response.json())
    else:
        print("Failed to retrieve data.")


# Run the functions
if __name__ == "__main__":
    send_data(post_url)

    get_data(get_url)
