"""Base service for simple REST interactions"""
import logging
import json
import requests

def create_logger():
    """logger"""
    log = logging.getLogger()
    log.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    log.addHandler(console_handler)
    return log

logger = create_logger()

class BaseService:
    """Base API service behaviour"""
    def delete(self, url, headers, timeout=10):
        """Delete method"""
        try:
            response = requests.delete(url, headers=headers, timeout=timeout)
            response.raise_for_status()
            logger.info("OK. URL: %s, Code: %d", url, response.status_code)
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error("Error. %s", str(e))
            return None


    def post(self, url, body, timeout = 10):
        """Post method"""
        try:
            headers = {'accept': "application/json", 'Content-Type': 'application/json'}
            response = requests.post(url, data=json.dumps(body), headers=headers, timeout=timeout)
            response.raise_for_status()
            logger.info("OK. URL: %s, Code: %d", url, response.status_code)
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error("Error. %s", str(e))
            return None


    def put(self, url, body, headers, timeout = 10):
        """Put method"""
        try:
            response = requests.put(url, data=json.dumps(body), headers=headers, timeout=timeout)
            response.raise_for_status()
            logger.info("OK. URL: %s, Code: %d", url, response.status_code)
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error("Error. %s", str(e))
            return None


    def get(self, url, params=None, headers=None, timeout = 10):
        """Get method"""
        try:
            response = requests.get(url, params=params, headers=headers, timeout=timeout)
            response.raise_for_status()
            logger.info("OK. URL: %s, Code: %d", url, response.status_code)
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error("Error. %s", str(e))
            return None
