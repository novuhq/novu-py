import requests
from typing import Optional, Tuple, Union
from .types import BeforeRequestContext, BeforeRequestHook, AfterSuccessContext, AfterSuccessHook, AfterErrorContext, AfterErrorHook, SDKInitHook
import time
import random
import json

class NovuHooks(SDKInitHook, BeforeRequestHook, AfterSuccessHook, AfterErrorHook):
    def sdk_init(self, base_url: str, client: requests.Session) -> Tuple[str, requests.Session]:
        """
        Modify the base_url or wrap the client used by the SDK here and return the updated values.
        """
        return base_url, client

    def before_request(self, hook_ctx: BeforeRequestContext, request: requests.PreparedRequest) -> Union[requests.PreparedRequest, Exception]:
        """
        Modify the request headers before sending it.
        """
        auth_key = 'Authorization'
        idempotency_key = 'idempotency-key'
        api_key_prefix = 'ApiKey'

        # Ensure headers exist and are a dictionary-like object
        if not hasattr(request, 'headers') or not isinstance(request.headers, dict):
            request.headers = {}

        # Check if the authorization header exists and modify it if necessary
        if auth_key in request.headers:
            key = request.headers[auth_key]
            if key and not key.startswith(api_key_prefix):
                request.headers[auth_key] = f"{api_key_prefix} {key}"

        # Check if headers exist and update the idempotency key if necessary
        if idempotency_key not in request.headers or not request.headers[idempotency_key]:
            request.headers[idempotency_key] = self.generate_idempotency_key()

        return request

    def after_success(self, hook_ctx: AfterSuccessContext, response: requests.Response) -> Union[requests.Response, Exception]:
        """
        Modify the response after a successful request.
        """
        # Clone the response and check its content type
        content_type = response.headers.get('Content-Type', '')

        if response.text == '' or 'text/html' in content_type:
            return response

        try:
            json_response = response.json()
        except ValueError:  # Handle JSONDecodeError
            return response

        # Check if the response contains a single 'data' key
        if isinstance(json_response, dict) and len(json_response) == 1 and 'data' in json_response:
            # Create a new response with just the 'data' content
            new_response = requests.Response()
            new_response.status_code = response.status_code
            new_response.headers = response.headers
            new_response.reason = response.reason
            new_response._content = json.dumps(json_response['data']).encode('utf-8')  # Encode to bytes
            return new_response

        return response

    def after_error(self, hook_ctx: AfterErrorContext, response: Optional[requests.Response], error: Optional[Exception]) -> Union[Tuple[Optional[requests.Response], Optional[Exception]], Exception]:
        """
        Modify the response or error after a failed request.
        """
        # Modify the response or error before returning
        if response is None and error is None:
            return ValueError("Both response and error cannot be None")
        return (response, error)

    def generate_idempotency_key(self) -> str:
        """
        Generate a unique idempotency key using a timestamp and a random string.
        """
        timestamp = int(time.time() * 1000)  # Current time in milliseconds
        random_string = ''.join(random.sample('abcdefghijklmnopqrstuvwxyz0123456789', 9))  # Unique alphanumeric string
        return f"{timestamp}{random_string}"  # Combine timestamp and random string