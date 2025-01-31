"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from .sdkconfiguration import SDKConfiguration
from novu_py import models, utils
from novu_py._hooks import HookContext
from novu_py.stats import Stats
from novu_py.types import BaseModel, OptionalNullable, UNSET
from novu_py.utils import get_security_from_env
from typing import Any, Mapping, Optional, Union, cast


class Notifications(BaseSDK):
    stats: Stats

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        BaseSDK.__init__(self, sdk_config)
        self.sdk_configuration = sdk_config
        self._init_sdks()

    def _init_sdks(self):
        self.stats = Stats(self.sdk_configuration)

    def list(
        self,
        *,
        request: Union[
            models.NotificationsControllerListNotificationsRequest,
            models.NotificationsControllerListNotificationsRequestTypedDict,
        ] = models.NotificationsControllerListNotificationsRequest(),
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.NotificationsControllerListNotificationsResponse:
        r"""Get notifications

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

        if not isinstance(request, BaseModel):
            request = utils.unmarshal(
                request, models.NotificationsControllerListNotificationsRequest
            )
        request = cast(models.NotificationsControllerListNotificationsRequest, request)

        req = self._build_request(
            method="GET",
            path="/v1/notifications",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
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
                operation_id="NotificationsController_listNotifications",
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

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return models.NotificationsControllerListNotificationsResponse(
                result=utils.unmarshal_json(
                    http_res.text, models.ActivitiesResponseDto
                ),
                headers=utils.get_response_headers(http_res.headers),
            )
        if utils.match_response(http_res, "414", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ErrorDtoData)
            raise models.ErrorDto(data=data)
        if utils.match_response(
            http_res,
            ["400", "401", "403", "404", "405", "409", "413", "415"],
            "application/json",
        ):
            data = utils.unmarshal_json(http_res.text, models.ErrorDtoData)
            raise models.ErrorDto(data=data)
        if utils.match_response(http_res, "422", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ValidationErrorDtoData)
            raise models.ValidationErrorDto(data=data)
        if utils.match_response(http_res, "429", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "500", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ErrorDtoData)
            raise models.ErrorDto(data=data)
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

    async def list_async(
        self,
        *,
        request: Union[
            models.NotificationsControllerListNotificationsRequest,
            models.NotificationsControllerListNotificationsRequestTypedDict,
        ] = models.NotificationsControllerListNotificationsRequest(),
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.NotificationsControllerListNotificationsResponse:
        r"""Get notifications

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

        if not isinstance(request, BaseModel):
            request = utils.unmarshal(
                request, models.NotificationsControllerListNotificationsRequest
            )
        request = cast(models.NotificationsControllerListNotificationsRequest, request)

        req = self._build_request_async(
            method="GET",
            path="/v1/notifications",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
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
                operation_id="NotificationsController_listNotifications",
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

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return models.NotificationsControllerListNotificationsResponse(
                result=utils.unmarshal_json(
                    http_res.text, models.ActivitiesResponseDto
                ),
                headers=utils.get_response_headers(http_res.headers),
            )
        if utils.match_response(http_res, "414", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ErrorDtoData)
            raise models.ErrorDto(data=data)
        if utils.match_response(
            http_res,
            ["400", "401", "403", "404", "405", "409", "413", "415"],
            "application/json",
        ):
            data = utils.unmarshal_json(http_res.text, models.ErrorDtoData)
            raise models.ErrorDto(data=data)
        if utils.match_response(http_res, "422", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ValidationErrorDtoData)
            raise models.ValidationErrorDto(data=data)
        if utils.match_response(http_res, "429", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "500", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ErrorDtoData)
            raise models.ErrorDto(data=data)
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

    def retrieve(
        self,
        *,
        notification_id: str,
        idempotency_key: Optional[str] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.NotificationsControllerGetNotificationResponse:
        r"""Get notification

        :param notification_id:
        :param idempotency_key: A header for idempotency purposes
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

        request = models.NotificationsControllerGetNotificationRequest(
            notification_id=notification_id,
            idempotency_key=idempotency_key,
        )

        req = self._build_request(
            method="GET",
            path="/v1/notifications/{notificationId}",
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
                operation_id="NotificationsController_getNotification",
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

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return models.NotificationsControllerGetNotificationResponse(
                result=utils.unmarshal_json(
                    http_res.text, models.ActivityNotificationResponseDto
                ),
                headers=utils.get_response_headers(http_res.headers),
            )
        if utils.match_response(http_res, "414", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ErrorDtoData)
            raise models.ErrorDto(data=data)
        if utils.match_response(
            http_res,
            ["400", "401", "403", "404", "405", "409", "413", "415"],
            "application/json",
        ):
            data = utils.unmarshal_json(http_res.text, models.ErrorDtoData)
            raise models.ErrorDto(data=data)
        if utils.match_response(http_res, "422", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ValidationErrorDtoData)
            raise models.ValidationErrorDto(data=data)
        if utils.match_response(http_res, "429", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "500", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ErrorDtoData)
            raise models.ErrorDto(data=data)
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

    async def retrieve_async(
        self,
        *,
        notification_id: str,
        idempotency_key: Optional[str] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.NotificationsControllerGetNotificationResponse:
        r"""Get notification

        :param notification_id:
        :param idempotency_key: A header for idempotency purposes
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

        request = models.NotificationsControllerGetNotificationRequest(
            notification_id=notification_id,
            idempotency_key=idempotency_key,
        )

        req = self._build_request_async(
            method="GET",
            path="/v1/notifications/{notificationId}",
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
                operation_id="NotificationsController_getNotification",
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

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return models.NotificationsControllerGetNotificationResponse(
                result=utils.unmarshal_json(
                    http_res.text, models.ActivityNotificationResponseDto
                ),
                headers=utils.get_response_headers(http_res.headers),
            )
        if utils.match_response(http_res, "414", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ErrorDtoData)
            raise models.ErrorDto(data=data)
        if utils.match_response(
            http_res,
            ["400", "401", "403", "404", "405", "409", "413", "415"],
            "application/json",
        ):
            data = utils.unmarshal_json(http_res.text, models.ErrorDtoData)
            raise models.ErrorDto(data=data)
        if utils.match_response(http_res, "422", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ValidationErrorDtoData)
            raise models.ValidationErrorDto(data=data)
        if utils.match_response(http_res, "429", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "500", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ErrorDtoData)
            raise models.ErrorDto(data=data)
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
