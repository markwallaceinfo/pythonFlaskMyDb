import requests

# backend_testing.py

import requests
import json

def test_backend(rest_api_url, new_user_data):
    try:
        # Post new user data to the REST API using POST method
        post_response = requests.post(f"{rest_api_url}/users/{new_user_data['id']}", json=new_user_data)
        post_response_data = post_response.json()

        # Check if the POST request was successful
        assert post_response.status_code == 200
        assert post_response_data["status"] == "ok"

        # Submit a GET request to the REST API to retrieve the posted data
        get_response = requests.get(f"{rest_api_url}/users/{new_user_data['id']}")
        get_response_data = get_response.json()

        # Check if the GET request was successful and data equals the posted data
        assert get_response.status_code == 200
        assert get_response_data["status"] == "ok"
        assert get_response_data["user_name"] == new_user_data["user_name"]

        print("Backend Testing Passed!")

    except Exception as e:
        print(f"Backend Testing Failed: {str(e)}")

    rest_api_url = "http://127.0.0.1:5000"  # Update with the actual REST API URL
    new_user_data = {"id": 9, "user_name": "test_user"}  # Replace with the new user data for testing
    test_backend(rest_api_url, new_user_data)





print("----------------")
# # Post a user on the database
# post_req = requests.post('http://127.0.0.1:500//users/1', json={"user_name": "john"})
# # Get user that was posted on database
# get_req = requests.get('http://127.0.0.1:500//users/1')
# # Check response code
# if get_req.status_code == 200:
#     print('user was created successfully')
# else:
#     raise Exception("user was not created")
