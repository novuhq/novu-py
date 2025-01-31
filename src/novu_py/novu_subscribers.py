"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from novu_py import models, utils
from novu_py._hooks import HookContext
from novu_py.types import OptionalNullable, UNSET
from novu_py.utils import get_security_from_env
from typing import Any, Mapping, Optional, Union


class NovuSubscribers(BaseSDK):
    def assign(
        self,
        *,
        topic_key: str,
        add_subscribers_request_dto: Union[
            models.AddSubscribersRequestDto, models.AddSubscribersRequestDtoTypedDict
        ],
        idempotency_key: Optional[str] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.TopicsControllerAssignResponse:
        r"""Subscribers addition

        Add subscribers to a topic by key

        :param topic_key: The topic key
        :param add_subscribers_request_dto:
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

        request = models.TopicsControllerAssignRequest(
            topic_key=topic_key,
            idempotency_key=idempotency_key,
            add_subscribers_request_dto=utils.get_pydantic_model(
                add_subscribers_request_dto, models.AddSubscribersRequestDto
            ),
        )

        req = self._build_request(
            method="POST",
            path="/v1/topics/{topicKey}/subscribers",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request.add_subscribers_request_dto,
                False,
                False,
                "json",
                models.AddSubscribersRequestDto,
            ),
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
                operation_id="TopicsController_assign",
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
            return models.TopicsControllerAssignResponse(
                result=utils.unmarshal_json(
                    http_res.text, models.AssignSubscriberToTopicDto
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

    async def assign_async(
        self,
        *,
        topic_key: str,
        add_subscribers_request_dto: Union[
            models.AddSubscribersRequestDto, models.AddSubscribersRequestDtoTypedDict
        ],
        idempotency_key: Optional[str] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.TopicsControllerAssignResponse:
        r"""Subscribers addition

        Add subscribers to a topic by key

        :param topic_key: The topic key
        :param add_subscribers_request_dto:
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

        request = models.TopicsControllerAssignRequest(
            topic_key=topic_key,
            idempotency_key=idempotency_key,
            add_subscribers_request_dto=utils.get_pydantic_model(
                add_subscribers_request_dto, models.AddSubscribersRequestDto
            ),
        )

        req = self._build_request_async(
            method="POST",
            path="/v1/topics/{topicKey}/subscribers",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request.add_subscribers_request_dto,
                False,
                False,
                "json",
                models.AddSubscribersRequestDto,
            ),
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
                operation_id="TopicsController_assign",
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
            return models.TopicsControllerAssignResponse(
                result=utils.unmarshal_json(
                    http_res.text, models.AssignSubscriberToTopicDto
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
        external_subscriber_id: str,
        topic_key: str,
        idempotency_key: Optional[str] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.TopicsControllerGetTopicSubscriberResponse:
        r"""Check topic subscriber

        Check if a subscriber belongs to a certain topic

        :param external_subscriber_id: The external subscriber id
        :param topic_key: The topic key
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

        request = models.TopicsControllerGetTopicSubscriberRequest(
            external_subscriber_id=external_subscriber_id,
            topic_key=topic_key,
            idempotency_key=idempotency_key,
        )

        req = self._build_request(
            method="GET",
            path="/v1/topics/{topicKey}/subscribers/{externalSubscriberId}",
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
                operation_id="TopicsController_getTopicSubscriber",
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
            return models.TopicsControllerGetTopicSubscriberResponse(
                result=utils.unmarshal_json(http_res.text, models.TopicSubscriberDto),
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
        external_subscriber_id: str,
        topic_key: str,
        idempotency_key: Optional[str] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.TopicsControllerGetTopicSubscriberResponse:
        r"""Check topic subscriber

        Check if a subscriber belongs to a certain topic

        :param external_subscriber_id: The external subscriber id
        :param topic_key: The topic key
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

        request = models.TopicsControllerGetTopicSubscriberRequest(
            external_subscriber_id=external_subscriber_id,
            topic_key=topic_key,
            idempotency_key=idempotency_key,
        )

        req = self._build_request_async(
            method="GET",
            path="/v1/topics/{topicKey}/subscribers/{externalSubscriberId}",
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
                operation_id="TopicsController_getTopicSubscriber",
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
            return models.TopicsControllerGetTopicSubscriberResponse(
                result=utils.unmarshal_json(http_res.text, models.TopicSubscriberDto),
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

    def remove(
        self,
        *,
        topic_key: str,
        remove_subscribers_request_dto: Union[
            models.RemoveSubscribersRequestDto,
            models.RemoveSubscribersRequestDtoTypedDict,
        ],
        idempotency_key: Optional[str] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.TopicsControllerRemoveSubscribersResponse:
        r"""Subscribers removal

        Remove subscribers from a topic

        :param topic_key: The topic key
        :param remove_subscribers_request_dto:
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

        request = models.TopicsControllerRemoveSubscribersRequest(
            topic_key=topic_key,
            idempotency_key=idempotency_key,
            remove_subscribers_request_dto=utils.get_pydantic_model(
                remove_subscribers_request_dto, models.RemoveSubscribersRequestDto
            ),
        )

        req = self._build_request(
            method="POST",
            path="/v1/topics/{topicKey}/subscribers/removal",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request.remove_subscribers_request_dto,
                False,
                False,
                "json",
                models.RemoveSubscribersRequestDto,
            ),
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
                operation_id="TopicsController_removeSubscribers",
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
        if utils.match_response(http_res, "204", "*"):
            return models.TopicsControllerRemoveSubscribersResponse(
                headers=utils.get_response_headers(http_res.headers)
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

    async def remove_async(
        self,
        *,
        topic_key: str,
        remove_subscribers_request_dto: Union[
            models.RemoveSubscribersRequestDto,
            models.RemoveSubscribersRequestDtoTypedDict,
        ],
        idempotency_key: Optional[str] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.TopicsControllerRemoveSubscribersResponse:
        r"""Subscribers removal

        Remove subscribers from a topic

        :param topic_key: The topic key
        :param remove_subscribers_request_dto:
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

        request = models.TopicsControllerRemoveSubscribersRequest(
            topic_key=topic_key,
            idempotency_key=idempotency_key,
            remove_subscribers_request_dto=utils.get_pydantic_model(
                remove_subscribers_request_dto, models.RemoveSubscribersRequestDto
            ),
        )

        req = self._build_request_async(
            method="POST",
            path="/v1/topics/{topicKey}/subscribers/removal",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request.remove_subscribers_request_dto,
                False,
                False,
                "json",
                models.RemoveSubscribersRequestDto,
            ),
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
                operation_id="TopicsController_removeSubscribers",
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
        if utils.match_response(http_res, "204", "*"):
            return models.TopicsControllerRemoveSubscribersResponse(
                headers=utils.get_response_headers(http_res.headers)
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
