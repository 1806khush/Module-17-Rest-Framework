import requests

# Function to fetch a random joke from the API
def fetch_joke():
    url = "https://v2.jokeapi.dev/joke/Any"  # Joke API URL
    params = {
        "type": "single",  # 'single' means only a one-liner joke
    }
    
    # Send GET request to the API
    response = requests.get(url, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        joke_data = response.json()
        
        # Check if the joke has a setup/punchline or a single part
        if joke_data.get("type") == "single":
            print("Joke: " + joke_data["joke"])
        elif joke_data.get("type") == "twopart":
            print("Setup: " + joke_data["setup"])
            print("Punchline: " + joke_data["delivery"])
    else:
        print("Failed to retrieve joke. Status code:", response.status_code)

# Call the function to fetch a joke
fetch_joke()
