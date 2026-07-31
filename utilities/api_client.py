import requests
from utilities.logger import Logger


class APIClient:

    def __init__(self):
        self.logger = Logger.get_logger()

    def get(self, url, headers=None, params=None, auth=None):
        try:
            self.logger.info(f"Sending GET request to {url}")
            response = requests.get(
                url,
                headers=headers,
                params=params,
                auth=auth,
                timeout=10
            )
            self.logger.info(f"Response Status Code: {response.status_code}")
            return response

        except requests.exceptions.RequestException as e:
            self.logger.error(f"GET request failed: {e}")
            raise

    def post(self, url, headers=None, json=None,auth=None):
        try:
            self.logger.info(f"Sending POST request to {url}")
            response = requests.post(
                url,
                headers=headers,
                json=json,
                auth=auth,
                timeout=10
            )
            self.logger.info(f"Response Status Code: {response.status_code}")
            return response

        except requests.exceptions.RequestException as e:
            self.logger.error(f"POST request failed: {e}")
            raise

    def put(self, url, headers=None, json=None,auth=None):
        try:
            self.logger.info(f"Sending PUT request to {url}")
            response = requests.put(
                url,
                headers=headers,
                json=json,
                auth=auth,
                timeout=10
            )
            self.logger.info(f"Response Status Code: {response.status_code}")
            return response

        except requests.exceptions.RequestException as e:
            self.logger.error(f"PUT request failed: {e}")
            raise

    def delete(self, url, headers=None,auth=None):
        try:
            self.logger.info(f"Sending DELETE request to {url}")
            response = requests.delete(
                url,
                headers=headers,
                auth=auth,
                timeout=10
            )
            self.logger.info(f"Response Status Code: {response.status_code}")
            return response

        except requests.exceptions.RequestException as e:
            self.logger.error(f"DELETE request failed: {e}")
            raise