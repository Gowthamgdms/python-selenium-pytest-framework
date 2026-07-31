from utilities.api_client import APIClient

api = APIClient()

def test_get_request():

   response=api.get("https://jsonplaceholder.typicode.com/posts/1")

   # Validate Status Code
   assert response.status_code == 200
   print("Status Code Validation Passed")

   # Validate Response Body
   response_json = response.json()

   assert response_json["id"] == 1
   print("ID Validation Passed")

   assert response_json["userId"] == 1
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
    assert response.status_code == 201
    print("POST Status Code Validation Passed")

    #Validate Response Body
    response_json = response.json()
    assert response_json["title"] == "API Testing"
    print("Title Validation Passed")

    assert response_json["body"] == "Learning API Automation"
    print("Body Validation Passed")
    assert response_json["userId"] == 1
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
    assert response.status_code == 200
    print("PUT Status Code Validation Passed")

    #Validate Response Body
    response_json = response.json()
    assert response_json["title"] == "Updated API Testing"

    assert response_json["body"] == "Updated Learning API Automation"
    print("Body Validation Passed")

    assert response_json["userId"] == 1
    print("User ID Validation Passed")

    print(response_json)



def test_delete_request():

    response=api.delete("https://jsonplaceholder.typicode.com/posts/1")

    #Validate Status Code
    assert response.status_code == 200
    print("DELETE Status Code Validation Passed")

    print("Resource Deleted Successfully")


















