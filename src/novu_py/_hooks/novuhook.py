import requests
import time
import random
import json
import io
from typing import Optional, Tuple, Union

from .types import (
    BeforeRequestContext,
    BeforeRequestHook,
    AfterSuccessContext,
    AfterSuccessHook,
    AfterErrorContext,
    AfterErrorHook,
    SDKInitHook
)

class NovuHooks(SDKInitHook, BeforeRequestHook, AfterSuccessHook, AfterErrorHook):
    def sdk_init(self, base_url: str, client: requests.Session) -> Tuple[str, requests.Session]:
        """
        Modify the base_url or wrap the client used by the SDK here and return the updated values.

        :param base_url: The original base URL
        :param client: The requests Session object
        :return: Tuple of potentially modified base_url and client
        """
        return base_url, client

    def before_request(self, hook_ctx: BeforeRequestContext, request: requests.PreparedRequest) -> Union[requests.PreparedRequest, Exception]:
        """
        Modify the request headers before sending it.

        :param hook_ctx: Context for the before request hook
        :param request: The prepared request to be modified
        :return: Modified request or an exception
        """
        auth_key = 'Authorization'
        idempotency_key = 'idempotency-key'
        api_key_prefix = 'ApiKey'

        # Ensure headers exist and are a dictionary-like object
        if not hasattr(request, 'headers') or request.headers is None:
            request.headers = {}

        # Check and modify authorization header
        if auth_key in request.headers:
            key = request.headers[auth_key]
            if key and not key.startswith(api_key_prefix):
                request.headers[auth_key] = f"{api_key_prefix} {key}"

        # Add idempotency key if not present
        if idempotency_key not in request.headers or not request.headers[idempotency_key]:
            request.headers[idempotency_key] = self.generate_idempotency_key()

        return request

    def after_success(self, hook_ctx: AfterSuccessContext, response: requests.Response) -> Union[requests.Response, Exception]:
        """
        Modify the response after a successful request.

        :param hook_ctx: Context for the after success hook
        :param response: The response to be potentially modified
        :return: Modified or original response
        """
        # Check content type
        content_type = response.headers.get('Content-Type', '')

        # Return early for empty or HTML responses
        if response.text == '' or 'text/html' in content_type:
            return response

        try:
            json_response = response.json()
        except ValueError:  # Handle JSONDecodeError
            return response

        # Check if the response contains a single 'data' key
        if isinstance(json_response, dict) and len(json_response) == 1 and 'data' in json_response:
            # Create a new response manually
            new_response = requests.Response()
            new_response.status_code = response.status_code
            new_response.headers = response.headers.copy()
            new_response.reason = response.reason
            new_response.url = response.url

            # Serialize the 'data' content
            data_content = json.dumps(json_response['data']).encode('utf-8')

            # Use io.BytesIO to set the raw content
            new_response.raw = io.BytesIO(data_content)

            return new_response

        return response

    def after_error(self, hook_ctx: AfterErrorContext, response: Optional[requests.Response], error: Optional[Exception]) -> Union[Tuple[Optional[requests.Response], Optional[Exception]], Exception]:
        """
        Modify the response or error after a failed request.

        :param hook_ctx: Context for the after error hook
        :param response: The response object (if any)
        :param error: The exception that occurred
        :return: Tuple of potentially modified response and error
        """
        # Validate input
        if response is None and error is None:
            return ValueError("Both response and error cannot be None")

        return (response, error)

    def generate_idempotency_key(self) -> str:
        """
        Generate a unique idempotency key using a timestamp and a random string.

        :return: A unique idempotency key
        """
        timestamp = int(time.time() * 1000)  # Current time in milliseconds
        random_string = ''.join(random.sample('abcdefghijklmnopqrstuvwxyz0123456789', 9))  # Unique alphanumeric string
        return f"{timestamp}{random_string}"
