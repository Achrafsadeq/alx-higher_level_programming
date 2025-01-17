#!/usr/bin/python3
"""
Python script that sends a POST request with a letter as a parameter
and processes the JSON response.
"""
import requests
import sys


def search_user(letter):
    url = "http://0.0.0.0:5000/search_user"
    payload = {'q': letter}

    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()  # Raise an error for bad status codes

        # Try to parse the response as JSON
        try:
            json_data = response.json()
            if json_data:
                print(f"[{json_data.get('id')}] {json_data.get('name')}")
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    search_user(letter)
