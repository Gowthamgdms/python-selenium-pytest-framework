class APIAssertions:

    @staticmethod
    def verify_status_code(response, expected_status_code):
        assert response.status_code == expected_status_code, (
            f"Expected Status Code: {expected_status_code}, "
            f"Actual Status Code: {response.status_code}"
        )

    @staticmethod
    def verify_header(response, header_name, expected_value):
        assert expected_value in response.headers.get(header_name, ""), (
            f"{header_name} validation failed"
        )

    @staticmethod
    def verify_key(response, key):
        response_json = response.json()
        assert key in response_json, (
            f"Key '{key}' not found in response"
        )

    @staticmethod
    def verify_value(response, key, expected_value):
        response_json = response.json()
        assert response_json[key] == expected_value, (
            f"Expected {key}={expected_value}, "
            f"Actual={response_json[key]}"
        )