# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------
from collections.abc import Awaitable
from typing import Callable, Any, Tuple, Generic, TypeVar

from ._poller import NoPolling as _NoPolling


PollingReturnType = TypeVar("PollingReturnType")


class AsyncPollingMethod(Generic[PollingReturnType]):
    """ABC class for polling method.
    """
    def initialize(self, client: Any, initial_response: Any, deserialization_callback: Any) -> None:
        raise NotImplementedError("This method needs to be implemented")

    async def run(self) -> None:
        raise NotImplementedError("This method needs to be implemented")

    def status(self) -> str:
        raise NotImplementedError("This method needs to be implemented")

    def finished(self) -> bool:
        raise NotImplementedError("This method needs to be implemented")

    def resource(self) -> PollingReturnType:
        raise NotImplementedError("This method needs to be implemented")

    def get_continuation_token(self) -> str:
        raise TypeError(
            "Polling method '{}' doesn't support get_continuation_token".format(
                self.__class__.__name__
            )
        )

    @classmethod
    def from_continuation_token(cls, continuation_token: str, **kwargs) -> Tuple[Any, Any, Callable]:
        raise TypeError(
            "Polling method '{}' doesn't support from_continuation_token".format(
                cls.__name__
            )
        )


class AsyncNoPolling(_NoPolling):
    """An empty async poller that returns the deserialized initial response.
    """
    async def run(self):
        """Empty run, no polling.
        Just override initial run to add "async"
        """


async def async_poller(client, initial_response, deserialization_callback, polling_method):
    """Async Poller for long running operations.

    .. deprecated:: 1.5.0
       Use :class:`AsyncLROPoller` instead.

    :param client: A pipeline service client.
    :type client: ~azure.core.PipelineClient
    :param initial_response: The initial call response
    :type initial_response: ~azure.core.pipeline.transport.AsyncHttpResponse
    :param deserialization_callback: A callback that takes a Response and return a deserialized object.
                                     If a subclass of Model is given, this passes "deserialize" as callback.
    :type deserialization_callback: callable or msrest.serialization.Model
    :param polling_method: The polling strategy to adopt
    :type polling_method: ~azure.core.polling.PollingMethod
    """
    poller = AsyncLROPoller(client, initial_response, deserialization_callback, polling_method)
    return await poller


class AsyncLROPoller(Awaitable, Generic[PollingReturnType]):
    """Async poller for long running operations.

    :param client: A pipeline service client
    :type client: ~azure.core.PipelineClient
    :param initial_response: The initial call response
    :type initial_response:
     ~azure.core.pipeline.transport.HttpResponse or ~azure.core.pipeline.transport.AsyncHttpResponse
    :param deserialization_callback: A callback that takes a Response and return a deserialized object.
                                     If a subclass of Model is given, this passes "deserialize" as callback.
    :type deserialization_callback: callable or msrest.serialization.Model
    :param polling_method: The polling strategy to adopt
    :type polling_method: ~azure.core.polling.AsyncPollingMethod
    """

    def __init__(
            self,
            client: Any,
            initial_response: Any,
            deserialization_callback: Callable,
            polling_method: AsyncPollingMethod[PollingReturnType]
        ):
        self._polling_method = polling_method

        # This implicit test avoids bringing in an explicit dependency on Model directly
        try:
            deserialization_callback = deserialization_callback.deserialize # type: ignore
        except AttributeError:
            pass

        self._polling_method.initialize(client, initial_response, deserialization_callback)

    async def _start(self):
        """Start the long running operation.
        """
        await self._polling_method.run()
        return self._polling_method.resource()

    def __await__(self):
        return self._start().__await__()

    def continuation_token(self) -> str:
        """Return a continuation token that allows to restart the poller later.

        :returns: An opaque continuation token
        :rtype: str
        """
        return self._polling_method.get_continuation_token()

    @classmethod
    def from_continuation_token(
            cls,
            polling_method: AsyncPollingMethod[PollingReturnType],
            continuation_token: str,
            **kwargs
        ) -> "AsyncLROPoller[PollingReturnType]":
        client, initial_response, deserialization_callback = polling_method.from_continuation_token(
            continuation_token, **kwargs
        )
        return cls(client, initial_response, deserialization_callback, polling_method)

    def status(self) -> str:
        """Returns the current status string.

        :returns: The current status string
        :rtype: str
        """
        return self._polling_method.status()
