# api_client.py (v2 - Updated for POST /queries endpoint )

import os
import requests
import time
from dotenv import load_dotenv

# --- Configuration ---
load_dotenv()
LIMITLESS_API_KEY = os.getenv("LIMITLESS_API_KEY")
BASE_API_URL = "https://api.limitless.ai/v1/"

# --- Core Functions ---

def check_api_key( ):
    """Checks if the API key was successfully loaded."""
    if not LIMITLESS_API_KEY:
        print("❌ ERROR: LIMITLESS_API_KEY not found in .env file.")
        return False
    print(f"✅ API Key loaded successfully (starts with: {LIMITLESS_API_KEY[:6]}...).")
    return True

def get_latest_meeting_transcript():
    """
    Connects to the Limitless API by creating a query to fetch the latest meeting.
    This matches the official API documentation.
    """
    if not check_api_key():
        return None

    # The correct endpoint according to the documentation
    endpoint = "queries" 
    url = BASE_API_URL + endpoint
    
    headers = {
        "Authorization": f"Bearer {LIMITLESS_API_KEY}",
        "Content-Type": "application/json"
    }

    # The "payload" or "body" of our request.
    # We are asking the AI a question in plain English.
    payload = {
        "prompt": "What was my last meeting and what is the full transcript?"
    }

    print("\n🔄 Sending query to Limitless API: 'What was my last meeting...?'")
    try:
        # Step 1: Create the query
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        
        query_creation_data = response.json()
        query_id = query_creation_data.get("id")

        if not query_id:
            print("❌ Failed to create a query. Response did not include an ID.")
            print(f"   Response: {query_creation_data}")
            return None
        
        print(f"✅ Query created successfully with ID: {query_id}")

        # Step 2: Poll for the result
        result_url = f"{url}/{query_id}"
        print(f"🔄 Polling for result at: {result_url}")
        
        while True:
            result_response = requests.get(result_url, headers=headers)
            result_response.raise_for_status()
            result_data = result_response.json()

            status = result_data.get("status")
            print(f"   Query status: {status}")

            if status == "completed":
                print("✅ Query completed!")
                # Assuming the answer is in a field called 'result' or 'answer'
                answer = result_data.get("result", {}).get("answer", "No answer found.")
                return answer
            
            if status in ["failed", "error"]:
                print(f"❌ Query failed with status: {status}")
                print(f"   Details: {result_data}")
                return None
            
            # Wait for 2 seconds before checking again
            time.sleep(2)

    except requests.exceptions.HTTPError as http_err:
        print(f"❌ HTTP Error occurred: {http_err}" )
        print(f"   Status Code: {http_err.response.status_code}" )
        print(f"   Response Text: {http_err.response.text}" )
        return None
    except Exception as err:
        print(f"❌ An unexpected error occurred: {err}")
        return None

# --- Self-Testing Block ---
if __name__ == "__main__":
    print("--- Running API Client Self-Test (v2) ---")
    transcript = get_latest_meeting_transcript()
    
    if transcript:
        print("\n--- Test Successful! ---")
        print("Retrieved Answer/Transcript:")
        print(transcript)
    else:
        print("\n--- Test Failed ---")
        print("Could not retrieve the answer. Please check the error messages above.")
