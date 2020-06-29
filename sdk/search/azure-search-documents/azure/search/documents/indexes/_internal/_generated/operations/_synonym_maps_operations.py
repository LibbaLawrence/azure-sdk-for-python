# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class SynonymMapsOperations(object):
    """SynonymMapsOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.search.documents.indexes.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def create_or_update(
        self,
        synonym_map_name,  # type: str
        synonym_map,  # type: "models.SynonymMap"
        if_match=None,  # type: Optional[str]
        if_none_match=None,  # type: Optional[str]
        request_options=None,  # type: Optional["models.RequestOptions"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.SynonymMap"
        """Creates a new synonym map or updates a synonym map if it already exists.

        :param synonym_map_name: The name of the synonym map to create or update.
        :type synonym_map_name: str
        :param synonym_map: The definition of the synonym map to create or update.
        :type synonym_map: ~azure.search.documents.indexes.models.SynonymMap
        :param if_match: Defines the If-Match condition. The operation will be performed only if the
         ETag on the server matches this value.
        :type if_match: str
        :param if_none_match: Defines the If-None-Match condition. The operation will be performed only
         if the ETag on the server does not match this value.
        :type if_none_match: str
        :param request_options: Parameter group.
        :type request_options: ~azure.search.documents.indexes.models.RequestOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SynonymMap, or the result of cls(response)
        :rtype: ~azure.search.documents.indexes.models.SynonymMap
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.SynonymMap"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        
        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id
        prefer = "return=representation"
        api_version = "2020-06-30"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.create_or_update.metadata['url']  # type: ignore
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'synonymMapName': self._serialize.url("synonym_map_name", synonym_map_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if _x_ms_client_request_id is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("x_ms_client_request_id", _x_ms_client_request_id, 'str')
        if if_match is not None:
            header_parameters['If-Match'] = self._serialize.header("if_match", if_match, 'str')
        if if_none_match is not None:
            header_parameters['If-None-Match'] = self._serialize.header("if_none_match", if_none_match, 'str')
        header_parameters['Prefer'] = self._serialize.header("prefer", prefer, 'str')
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(synonym_map, 'SynonymMap')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.SearchError, response)
            raise HttpResponseError(response=response, model=error)

        if response.status_code == 200:
            deserialized = self._deserialize('SynonymMap', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('SynonymMap', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_or_update.metadata = {'url': '/synonymmaps(\'{synonymMapName}\')'}  # type: ignore

    def delete(
        self,
        synonym_map_name,  # type: str
        if_match=None,  # type: Optional[str]
        if_none_match=None,  # type: Optional[str]
        request_options=None,  # type: Optional["models.RequestOptions"]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Deletes a synonym map.

        :param synonym_map_name: The name of the synonym map to delete.
        :type synonym_map_name: str
        :param if_match: Defines the If-Match condition. The operation will be performed only if the
         ETag on the server matches this value.
        :type if_match: str
        :param if_none_match: Defines the If-None-Match condition. The operation will be performed only
         if the ETag on the server does not match this value.
        :type if_none_match: str
        :param request_options: Parameter group.
        :type request_options: ~azure.search.documents.indexes.models.RequestOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        
        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id
        api_version = "2020-06-30"

        # Construct URL
        url = self.delete.metadata['url']  # type: ignore
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'synonymMapName': self._serialize.url("synonym_map_name", synonym_map_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if _x_ms_client_request_id is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("x_ms_client_request_id", _x_ms_client_request_id, 'str')
        if if_match is not None:
            header_parameters['If-Match'] = self._serialize.header("if_match", if_match, 'str')
        if if_none_match is not None:
            header_parameters['If-None-Match'] = self._serialize.header("if_none_match", if_none_match, 'str')

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204, 404]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.SearchError, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/synonymmaps(\'{synonymMapName}\')'}  # type: ignore

    def get(
        self,
        synonym_map_name,  # type: str
        request_options=None,  # type: Optional["models.RequestOptions"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.SynonymMap"
        """Retrieves a synonym map definition.

        :param synonym_map_name: The name of the synonym map to retrieve.
        :type synonym_map_name: str
        :param request_options: Parameter group.
        :type request_options: ~azure.search.documents.indexes.models.RequestOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SynonymMap, or the result of cls(response)
        :rtype: ~azure.search.documents.indexes.models.SynonymMap
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.SynonymMap"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        
        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id
        api_version = "2020-06-30"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'synonymMapName': self._serialize.url("synonym_map_name", synonym_map_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if _x_ms_client_request_id is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("x_ms_client_request_id", _x_ms_client_request_id, 'str')
        header_parameters['Accept'] = 'application/json'

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.SearchError, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('SynonymMap', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/synonymmaps(\'{synonymMapName}\')'}  # type: ignore

    def list(
        self,
        select=None,  # type: Optional[str]
        request_options=None,  # type: Optional["models.RequestOptions"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.ListSynonymMapsResult"
        """Lists all synonym maps available for a search service.

        :param select: Selects which top-level properties of the synonym maps to retrieve. Specified as
         a comma-separated list of JSON property names, or '*' for all properties. The default is all
         properties.
        :type select: str
        :param request_options: Parameter group.
        :type request_options: ~azure.search.documents.indexes.models.RequestOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ListSynonymMapsResult, or the result of cls(response)
        :rtype: ~azure.search.documents.indexes.models.ListSynonymMapsResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ListSynonymMapsResult"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        
        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id
        api_version = "2020-06-30"

        # Construct URL
        url = self.list.metadata['url']  # type: ignore
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if select is not None:
            query_parameters['$select'] = self._serialize.query("select", select, 'str')
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if _x_ms_client_request_id is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("x_ms_client_request_id", _x_ms_client_request_id, 'str')
        header_parameters['Accept'] = 'application/json'

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.SearchError, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('ListSynonymMapsResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    list.metadata = {'url': '/synonymmaps'}  # type: ignore

    def create(
        self,
        synonym_map,  # type: "models.SynonymMap"
        request_options=None,  # type: Optional["models.RequestOptions"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.SynonymMap"
        """Creates a new synonym map.

        :param synonym_map: The definition of the synonym map to create.
        :type synonym_map: ~azure.search.documents.indexes.models.SynonymMap
        :param request_options: Parameter group.
        :type request_options: ~azure.search.documents.indexes.models.RequestOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SynonymMap, or the result of cls(response)
        :rtype: ~azure.search.documents.indexes.models.SynonymMap
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.SynonymMap"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        
        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id
        api_version = "2020-06-30"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.create.metadata['url']  # type: ignore
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if _x_ms_client_request_id is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("x_ms_client_request_id", _x_ms_client_request_id, 'str')
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(synonym_map, 'SynonymMap')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.SearchError, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('SynonymMap', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create.metadata = {'url': '/synonymmaps'}  # type: ignore
