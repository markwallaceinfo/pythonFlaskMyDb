
from Backend_test import test_backend
from frontend_test import frontend_test
from db_connector import add_user


def combined_test(web_interface_url, rest_api_url, new_user_data):
    try:
        # Run Backend Testing
        test_backend(rest_api_url, new_user_data)

        # Using pymysql, check if posted data was stored inside the DB (users table)
        db_data = add_user(user_id=1, username='james')

        # Check if data in the database matches the posted data
        assert db_data is not None
        assert db_data[1] == new_user_data['user_name']

        # Start a Selenium Webdriver session
        frontend_test(web_interface_url, new_user_data['id'])

        print("Combined Testing Passed!")

    except Exception as e:
        raise Exception(f"Combined Testing Failed: {str(e)}")

    web_interface_url = "http://127.0.0.1:5001"  # Update with the actual web interface URL
    rest_api_url = "http://127.0.0.1:5000"  # Update with the actual REST API URL
    new_user_data = {"id": 10, "user_name": "test_user"}  # Replace with the new user data for testing

    combined_test(web_interface_url, rest_api_url, new_user_data)
