import requests
import json
import time
import logging
from requests.adapters import HTTPAdapter  # HTTPAdapter is used to configure and attach retry logic to requests sessions
from urllib3.util.retry import Retry  # Retry is used to define the retry policy, including the number of retries and which HTTP status codes to retry on


# Set up the logging configuration
logging.basicConfig(
    level=logging.INFO,  # Set the logging level to INFO, meaning messages with severity INFO or higher will be logged
    format='%(asctime)s - %(levelname)s - %(message)s',  # Format the log messages to include timestamp, log level, and the message
    handlers=[
        logging.FileHandler("megaverse.log"),  # Log messages will be written to the file "megaverse.log"
        logging.StreamHandler()  # Log messages will also be displayed on the console (standard output)
    ]
)


class MegaverseAPI:
    """Handles interaction with the Megaverse API"""
    
    
    # Initializes the API class with the candidate ID, sets up a session with retry logic, and configures headers for JSON requests.
    def __init__(self, candidate_id):
        self.candidate_id = candidate_id
        self.base_url = "https://challenge.crossmint.io/api"
        self.headers = {"Content-Type": "application/json"}
        
        # Session setup with retry logic
        self.session = requests.Session()
        retries = Retry(total=3,  # Retry up to 3 times
                        backoff_factor=1,  # Wait 1 second between retries
                        status_forcelist=[429, 500, 502, 503, 504],
                        allowed_methods=["HEAD", "GET", "OPTIONS", "POST"])  # Retry on server errors
        adapter = HTTPAdapter(max_retries=retries)

        #mount adapter for both https and http requests
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)
    

    def get_goal_map(self):
    
        """Fetch the goal map for the candidate"""
    
        api_url = f"{self.base_url}/map/{self.candidate_id}/goal"

        try:
            response = self.session.get(api_url)
            response.raise_for_status()  # it will raise an HTTPError if the HTTP request returned an unsuccessful status code (4xx or 5xx), ensuring that any failed request is properly caught and handled.
            logging.info("Successfully fetched goal map")
            return response.json().get('goal', [])
        
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching goal map: {e}")
            return []
    
    
    
    def post_object(self, object_type, row, column, **kwargs):
    
        """A generic function to post any celestial object (Polyanets, Soloons, Comeths) to the API, 
        consolidating logic for all objects into one function to avoid duplication. 
        Each object's creation is managed by the Build_Megaverse class."""

    
        api_url = f"{self.base_url}/{object_type}"
        data = {"row": row, "column": column, "candidateId": self.candidate_id}
        data.update(kwargs)  # Add extra arguments like color or direction for soloon & cometh
        
        try:
            response = self.session.post(api_url, data=json.dumps(data), headers=self.headers)
            response.raise_for_status()
            logging.info(f"Successfully created {object_type} at ({row}, {column})")

        except requests.exceptions.RequestException as e:
            logging.error(f"Error creating {object_type} at ({row}, {column}): {e}")





class Build_Megaverse:
    """Handles the logic to construct the megaverse"""
    
    def __init__(self, api_client):
        self.api_client = api_client
    
    def process_map(self, matrix):
        """Process the goal map and create celestial objects based on the map"""
        
        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                object_type = matrix[row][column].lower()

                if object_type == "space":
                    continue  # Skip empty space

                if object_type == "polyanet":
                    self.api_client.post_object("polyanets", row, column)

                elif "soloon" in object_type:
                    color = object_type.split('_')[0]
                    self.api_client.post_object("soloons", row, column, color=color)

                elif "cometh" in object_type:
                    direction = object_type.split('_')[0]
                    self.api_client.post_object("comeths", row, column, direction=direction)
                
                time.sleep(0.3)  # To avoid too many API requests in a short time


def main():
    # Set up API client
    # Start timing
    start_time = time.time()
    candidate_id = "fccfd8da-ffec-4bf2-a1c7-8770ab1a7a76"
    api_client = MegaverseAPI(candidate_id)
    
    # Fetch goal map
    goal_map = api_client.get_goal_map()
    if not goal_map:
        print("Failed to retrieve goal map.")
        return
    
    # Process the map and create the required objects
    builder = Build_Megaverse(api_client)
    builder.process_map(goal_map)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Total execution time: {elapsed_time:.2f} seconds")
    logging.info(f"Total execution time: {elapsed_time:.2f} seconds")


if __name__ == "__main__":
    main()
