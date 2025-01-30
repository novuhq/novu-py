from typing import Optional, Tuple, Union, Dict, Any
import time
import random
import json
import http.client
import urllib.parse

from .types import (
    BeforeRequestContext,
    BeforeRequestHook,
    AfterSuccessContext,
    AfterSuccessHook,
    AfterErrorContext,
    AfterErrorHook,
    SDKInitHook,
    HttpClient
)
class PreparedRequest:
    def __init__(self, method: str, url: str, headers: Optional[Dict[str, str]] = None, body: str = ''):
        self.method = method
        self.url = url
        self.headers = {k: v for k, v in (headers or {}).items()}
        self.body = body

class Response:
    def __init__(self, status_code: int = 200, headers: Optional[Dict[str, str]]= None, text: str = '', reason: str = ''):
        self.status_code = status_code
        self.headers = {k: v for k, v in (headers or {}).items()}
        self.text = text
        self.reason = reason
        self.encoding = 'utf-8'
        self.raw = None

    def json(self):
        return json.loads(self.text) if self.text else {}

class Session:
    def prepare_request(self, method: str, url: str, headers: Optional[Dict[str, str]] = None, data: Any = None):
        """
        Prepare a request without using requests library
        """

        # Prepare headers
        prepared_headers = {k: v for k, v in (headers or {}).items()}

        # Prepare body
        body = json.dumps(data) if data and isinstance(data, (dict, list)) else data

        return PreparedRequest(method, url, prepared_headers, body)

    def send(self, prepared_request: PreparedRequest) -> Response:
        """
        Send a prepared request and return a response
        """
        # Parse the URL
        parsed_url = urllib.parse.urlparse(prepared_request.url)

        # Determine connection type
        if parsed_url.scheme == 'https':
            conn = http.client.HTTPSConnection(parsed_url.netloc)
        else:
            conn = http.client.HTTPConnection(parsed_url.netloc)

        try:
            # Send the request
            conn.request(
                prepared_request.method,
                parsed_url.path + ('?' + parsed_url.query if parsed_url.query else ''),
                body=prepared_request.body,
                headers=prepared_request.headers
            )

            # Get the response
            http_response = conn.getresponse()

            # Read response body
            response_body = http_response.read().decode('utf-8')

            # Create our custom Response object
            response = Response(
                status_code=http_response.status,
                headers=dict(http_response.getheaders()),
                text=response_body,
                reason=http_response.reason
            )

            return response
        finally:
            conn.close()

class NovuHooks(SDKInitHook, BeforeRequestHook, AfterSuccessHook, AfterErrorHook):
    def sdk_init(self, base_url: str, client: HttpClient) -> Tuple[str, HttpClient]:
        """
        Modify the base_url or wrap the client used by the SDK here and return the updated values.
        """
        return base_url, client

    def before_request(self, hook_ctx: BeforeRequestContext, request: PreparedRequest) -> Union[PreparedRequest, Exception]:
        """
        Modify the request headers before sending it.
        """
        auth_key = 'Authorization'
        idempotency_key = 'idempotency-key'
        api_key_prefix = 'ApiKey'

        # Ensure headers exist and are a dictionary
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

    def after_success(self, hook_ctx: AfterSuccessContext, response: Response) -> Union[Response, Exception]:
        """
        Modify the response after a successful request.
        """
        # Check content type
        content_type = response.headers.get('Content-Type', '')

        if response.text == '' or 'text/html' in content_type:
            return response

        try:
            json_response = response.json()
        except (ValueError, json.JSONDecodeError):  # Handle JSONDecodeError
            return response

        # Check if the response contains a single 'data' key
        if isinstance(json_response, dict) and len(json_response) == 1 and 'data' in json_response:
            # Create a new response with just the 'data' content
            new_response = Response(
                status_code=response.status_code,
                headers=response.headers,
                text=json.dumps(json_response['data']),
                reason=response.reason
            )
            return new_response

        return response

    def after_error(self, hook_ctx: AfterErrorContext, response: Optional[Response], error: Optional[Exception]) -> Union[Tuple[Optional[Response], Optional[Exception]], Exception]:
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
