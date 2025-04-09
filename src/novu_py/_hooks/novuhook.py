import json
import random
import time
from typing import Union

import httpx

from .types import (
    BeforeRequestHook,
    AfterSuccessHook,
    BeforeRequestContext,
    AfterSuccessContext
)


def generate_idempotency_key():
    """
    Generate a unique idempotency key.

    :return: A unique idempotency key as a string
    """
    timestamp = int(time.time() * 1000)  # Current time in milliseconds
    random_string = ''.join(random.sample('abcdefghijklmnopqrstuvwxyz0123456789', 9))  # Unique alphanumeric string
    return f"{timestamp}{random_string}"

def clean_headers(headers: dict) -> dict:
    """
    Remove problematic headers from the response.

    :param headers: Original headers
    :return: Cleaned headers
    """
    headers.pop('content-encoding', None)
    headers.pop('transfer-encoding', None)
    return headers

class NovuHooks(BeforeRequestHook, AfterSuccessHook):
    def before_request(self, hook_ctx: BeforeRequestContext, request: httpx.Request) -> Union[httpx.Request, Exception]:
        """
        Modify the request before sending.

        :param hook_ctx: Context for the before request hook
        :param request: The request to be modified
        :return: Modified request
        """
        auth_key = 'authorization'
        idempotency_key = 'idempotency-key'
        api_key_prefix = 'ApiKey'

        # Create a copy of headers
        headers = dict(request.headers or {})

        # Check and modify authorization header
        if auth_key in headers:
            key = headers[auth_key]
            if key and not key.startswith(api_key_prefix):
                headers[auth_key] = f"{api_key_prefix} {key}"

        # Add idempotency key if not present
        if idempotency_key not in headers or not headers[idempotency_key]:
            headers[idempotency_key] = generate_idempotency_key()

        # Recreate the request with modified headers
        return httpx.Request(
            method=request.method,
            url=request.url,
            headers=headers,
            content=request.content,
            extensions=request.extensions
        )

    def after_success(self, hook_ctx: AfterSuccessContext, response: httpx.Response) -> Union[httpx.Response, Exception]:
        """
        Modify the response after a successful request.

        - Removes problematic headers.
        - Extracts the 'data' key if the response contains only that key.

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
            # Create a new HTTPX response
            new_response = httpx.Response(
                status_code=response.status_code,
                headers=clean_headers(dict(response.headers)),
                content=json.dumps(json_response['data']).encode('utf-8'),
                request=response.request
            )
            return new_response

        return response
