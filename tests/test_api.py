from utilities.api_assertions import APIAssertions
from utilities.api_client import APIClient

api = APIClient()

def test_get_request():

   response=api.get("https://jsonplaceholder.typicode.com/posts/1")

   # Validate Status Code
   APIAssertions.verify_status_code(response, 200)
   print("Status Code Validation Passed")

   # Validate Response Header
   APIAssertions.verify_header(response, "Content-Type", "application/json")
   print("Content-Type Validation Passed")

   # Validate Response Body
   response_json = response.json()

   APIAssertions.verify_value(response,"id",1)
   print("ID Validation Passed")

   APIAssertions.verify_value(response,"userId", 1)
   print("User ID Validation Passed")

   print(response_json)




def test_post_request():
    payload = {
        "title": "API Testing",
        "body": "Learning API Automation",
        "userId": 1
    }

    response=api.post("https://jsonplaceholder.typicode.com/posts",json=payload)

    #Validate Status Code
    APIAssertions.verify_status_code(response, 201)
    print("POST Status Code Validation Passed")

    #Validate Response Body
    response_json = response.json()
    APIAssertions.verify_value(response, "title", "API Testing")
    print("Title Validation Passed")

    APIAssertions.verify_value(response, "body", "Learning API Automation")
    print("Body Validation Passed")
    APIAssertions.verify_value(response, "userId", 1)
    print("User ID Validation Passed")

    print(response_json)




def test_put_request():
    payload = {
        "id": 1,
        "title": "Updated API Testing",
        "body": "Updated Learning API Automation",
        "userId": 1
    }
    response= api.put("https://jsonplaceholder.typicode.com/posts/1",json=payload)

    #Validate Status Code
    APIAssertions.verify_status_code(response, 200)
    print("PUT Status Code Validation Passed")

    #Validate Response Body
    response_json = response.json()
    APIAssertions.verify_value(response, "title", "Updated API Testing")

    APIAssertions.verify_value(response, "body", "Updated Learning API Automation")
    print("Body Validation Passed")

    APIAssertions.verify_value(response, "userId", 1)
    print("User ID Validation Passed")

    print(response_json)



def test_delete_request():

    response=api.delete("https://jsonplaceholder.typicode.com/posts/1")

    #Validate Status Code
    APIAssertions.verify_status_code(response, 200)
    print("DELETE Status Code Validation Passed")

    print("Resource Deleted Successfully")



def test_query_parameters():
    params = {
        "userId": 1,
    }
    response = api.get("https://jsonplaceholder.typicode.com/posts", params=params)

    # Validate Status Code
    APIAssertions.verify_status_code(response, 200)
    print("Status Code Validation Passed")

    response_json = response.json()

    #Validate all returned posts belong to userId = 1
    for post in response_json:
        assert post["userId"] == 1

    print("Query Parameter Validation Passed")



















