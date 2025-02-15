# run_api_call.py
import os
import requests



def make_api_call(): 
    api_url = "https://httpbin.org/get"
    api_key = os.getenv("API_KEY")
    
    if not api_key:
        raise ValueError("API_KEY is not set!")
    
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.get(api_url, headers=headers)
    
    if response.status_code == 200:
        print("API call successful:", response.json())
    else:
        print("API call failed:", response.status_code, response.text)

if __name__ == "__main__":
    make_api_call()
