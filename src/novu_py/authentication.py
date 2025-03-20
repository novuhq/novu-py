"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from enum import Enum
from novu_py import models, utils
from novu_py._hooks import HookContext
from novu_py.types import BaseModel, OptionalNullable, UNSET
from novu_py.utils import get_security_from_env
from typing import Any, Mapping, Optional, Union, cast


class ChatAccessOauthCallBackAcceptEnum(str, Enum):
    APPLICATION_JSON = "application/json"
    TEXT_HTML = "text/html"


class Authentication(BaseSDK):
    def chat_access_oauth(
        self,
        *,
        request: Union[
            models.SubscribersV1ControllerChatAccessOauthRequest,
            models.SubscribersV1ControllerChatAccessOauthRequestTypedDict,
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.SubscribersV1ControllerChatAccessOauthResponse:
        r"""Handle chat oauth

        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        if not isinstance(request, BaseModel):
            request = utils.unmarshal(
                request, models.SubscribersV1ControllerChatAccessOauthRequest
            )
        request = cast(models.SubscribersV1ControllerChatAccessOauthRequest, request)

        req = self._build_request(
            method="GET",
            path="/v1/subscribers/{subscriberId}/credentials/{providerId}/oauth",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config
            else:
                retries = utils.RetryConfig(
                    "backoff", utils.BackoffStrategy(1000, 30000, 1.5, 3600000), True
                )

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["408", "409", "429", "5XX"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                base_url=base_url or "",
                operation_id="SubscribersV1Controller_chatAccessOauth",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=[
                "400",
                "401",
                "403",
                "404",
                "405",
                "409",
                "413",
                "414",
                "415",
                "422",
                "429",
                "4XX",
                "500",
                "503",
                "5XX",
            ],
            retry_config=retry_config,
        )

        response_data: Any = None
        if utils.match_response(http_res, "200", "*"):
            return models.SubscribersV1ControllerChatAccessOauthResponse(headers={})
        if utils.match_response(http_res, "414", "application/json"):
            response_data = utils.unmarshal_json(http_res.text, models.ErrorDtoData)
            raise models.ErrorDto(data=response_data)
        if utils.match_response(
            http_res,
            ["400", "401", "403", "404", "405", "409", "413", "415"],
            "application/json",
        ):
            response_data = utils.unmarshal_json(http_res.text, models.ErrorDtoData)
            raise models.ErrorDto(data=response_data)
        if utils.match_response(http_res, "422", "application/json"):
            response_data = utils.unmarshal_json(
                http_res.text, models.ValidationErrorDtoData
            )
            raise models.ValidationErrorDto(data=response_data)
        if utils.match_response(http_res, "429", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "500", "application/json"):
            response_data = utils.unmarshal_json(http_res.text, models.ErrorDtoData)
            raise models.ErrorDto(data=response_data)
        if utils.match_response(http_res, "503", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "4XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = utils.stream_to_text(http_res)
        raise models.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    async def chat_access_oauth_async(
        self,
        *,
        request: Union[
            models.SubscribersV1ControllerChatAccessOauthRequest,
            models.SubscribersV1ControllerChatAccessOauthRequestTypedDict,
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.SubscribersV1ControllerChatAccessOauthResponse:
        r"""Handle chat oauth

        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        if not isinstance(request, BaseModel):
            request = utils.unmarshal(
                request, models.SubscribersV1ControllerChatAccessOauthRequest
            )
        request = cast(models.SubscribersV1ControllerChatAccessOauthRequest, request)

        req = self._build_request_async(
            method="GET",
            path="/v1/subscribers/{subscriberId}/credentials/{providerId}/oauth",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config
            else:
                retries = utils.RetryConfig(
                    "backoff", utils.BackoffStrategy(1000, 30000, 1.5, 3600000), True
                )

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["408", "409", "429", "5XX"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                base_url=base_url or "",
                operation_id="SubscribersV1Controller_chatAccessOauth",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=[
                "400",
                "401",
                "403",
                "404",
                "405",
                "409",
                "413",
                "414",
                "415",
                "422",
                "429",
                "4XX",
                "500",
                "503",
                "5XX",
            ],
            retry_config=retry_config,
        )

        response_data: Any = None
        if utils.match_response(http_res, "200", "*"):
            return models.SubscribersV1ControllerChatAccessOauthResponse(headers={})
        if utils.match_response(http_res, "414", "application/json"):
            response_data = utils.unmarshal_json(http_res.text, models.ErrorDtoData)
            raise models.ErrorDto(data=response_data)
        if utils.match_response(
            http_res,
            ["400", "401", "403", "404", "405", "409", "413", "415"],
            "application/json",
        ):
            response_data = utils.unmarshal_json(http_res.text, models.ErrorDtoData)
            raise models.ErrorDto(data=response_data)
        if utils.match_response(http_res, "422", "application/json"):
            response_data = utils.unmarshal_json(
                http_res.text, models.ValidationErrorDtoData
            )
            raise models.ValidationErrorDto(data=response_data)
        if utils.match_response(http_res, "429", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "500", "application/json"):
            response_data = utils.unmarshal_json(http_res.text, models.ErrorDtoData)
            raise models.ErrorDto(data=response_data)
        if utils.match_response(http_res, "503", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "4XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise models.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    def chat_access_oauth_call_back(
        self,
        *,
        request: Union[
            models.SubscribersV1ControllerChatOauthCallbackRequest,
            models.SubscribersV1ControllerChatOauthCallbackRequestTypedDict,
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        accept_header_override: Optional[ChatAccessOauthCallBackAcceptEnum] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.SubscribersV1ControllerChatOauthCallbackResponse:
        r"""Handle providers oauth redirect

        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param accept_header_override: Override the default accept header for this method
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        if not isinstance(request, BaseModel):
            request = utils.unmarshal(
                request, models.SubscribersV1ControllerChatOauthCallbackRequest
            )
        request = cast(models.SubscribersV1ControllerChatOauthCallbackRequest, request)

        req = self._build_request(
            method="GET",
            path="/v1/subscribers/{subscriberId}/credentials/{providerId}/oauth/callback",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value=accept_header_override.value
            if accept_header_override is not None
            else "application/json;q=1, text/html;q=0",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config
            else:
                retries = utils.RetryConfig(
                    "backoff", utils.BackoffStrategy(1000, 30000, 1.5, 3600000), True
                )

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["408", "409", "429", "5XX"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                base_url=base_url or "",
                operation_id="SubscribersV1Controller_chatOauthCallback",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=[
                "400",
                "401",
                "403",
                "404",
                "405",
                "409",
                "413",
                "414",
                "415",
                "422",
                "429",
                "4XX",
                "500",
                "503",
                "5XX",
            ],
            retry_config=retry_config,
        )

        response_data: Any = None
        if utils.match_response(http_res, "200", "text/html"):
            return models.SubscribersV1ControllerChatOauthCallbackResponse(
                result=http_res.text,
                headers=utils.get_response_headers(http_res.headers),
            )
        if utils.match_response(http_res, "302", "application/json"):
            return models.SubscribersV1ControllerChatOauthCallbackResponse(
                result=utils.unmarshal_json(http_res.text, str),
                headers=utils.get_response_headers(http_res.headers),
            )
        if utils.match_response(http_res, "414", "application/json"):
            response_data = utils.unmarshal_json(http_res.text, models.ErrorDtoData)
            raise models.ErrorDto(data=response_data)
        if utils.match_response(
            http_res,
            ["400", "401", "403", "404", "405", "409", "413", "415"],
            "application/json",
        ):
            response_data = utils.unmarshal_json(http_res.text, models.ErrorDtoData)
            raise models.ErrorDto(data=response_data)
        if utils.match_response(http_res, "422", "application/json"):
            response_data = utils.unmarshal_json(
                http_res.text, models.ValidationErrorDtoData
            )
            raise models.ValidationErrorDto(data=response_data)
        if utils.match_response(http_res, "429", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "500", "application/json"):
            response_data = utils.unmarshal_json(http_res.text, models.ErrorDtoData)
            raise models.ErrorDto(data=response_data)
        if utils.match_response(http_res, "503", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "4XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = utils.stream_to_text(http_res)
        raise models.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    async def chat_access_oauth_call_back_async(
        self,
        *,
        request: Union[
            models.SubscribersV1ControllerChatOauthCallbackRequest,
            models.SubscribersV1ControllerChatOauthCallbackRequestTypedDict,
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        accept_header_override: Optional[ChatAccessOauthCallBackAcceptEnum] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.SubscribersV1ControllerChatOauthCallbackResponse:
        r"""Handle providers oauth redirect

        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param accept_header_override: Override the default accept header for this method
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        if not isinstance(request, BaseModel):
            request = utils.unmarshal(
                request, models.SubscribersV1ControllerChatOauthCallbackRequest
            )
        request = cast(models.SubscribersV1ControllerChatOauthCallbackRequest, request)

        req = self._build_request_async(
            method="GET",
            path="/v1/subscribers/{subscriberId}/credentials/{providerId}/oauth/callback",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value=accept_header_override.value
            if accept_header_override is not None
            else "application/json;q=1, text/html;q=0",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config
            else:
                retries = utils.RetryConfig(
                    "backoff", utils.BackoffStrategy(1000, 30000, 1.5, 3600000), True
                )

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["408", "409", "429", "5XX"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                base_url=base_url or "",
                operation_id="SubscribersV1Controller_chatOauthCallback",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=[
                "400",
                "401",
                "403",
                "404",
                "405",
                "409",
                "413",
                "414",
                "415",
                "422",
                "429",
                "4XX",
                "500",
                "503",
                "5XX",
            ],
            retry_config=retry_config,
        )

        response_data: Any = None
        if utils.match_response(http_res, "200", "text/html"):
            return models.SubscribersV1ControllerChatOauthCallbackResponse(
                result=http_res.text,
                headers=utils.get_response_headers(http_res.headers),
            )
        if utils.match_response(http_res, "302", "application/json"):
            return models.SubscribersV1ControllerChatOauthCallbackResponse(
                result=utils.unmarshal_json(http_res.text, str),
                headers=utils.get_response_headers(http_res.headers),
            )
        if utils.match_response(http_res, "414", "application/json"):
            response_data = utils.unmarshal_json(http_res.text, models.ErrorDtoData)
            raise models.ErrorDto(data=response_data)
        if utils.match_response(
            http_res,
            ["400", "401", "403", "404", "405", "409", "413", "415"],
            "application/json",
        ):
            response_data = utils.unmarshal_json(http_res.text, models.ErrorDtoData)
            raise models.ErrorDto(data=response_data)
        if utils.match_response(http_res, "422", "application/json"):
            response_data = utils.unmarshal_json(
                http_res.text, models.ValidationErrorDtoData
            )
            raise models.ValidationErrorDto(data=response_data)
        if utils.match_response(http_res, "429", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "500", "application/json"):
            response_data = utils.unmarshal_json(http_res.text, models.ErrorDtoData)
            raise models.ErrorDto(data=response_data)
        if utils.match_response(http_res, "503", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "4XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise models.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )
