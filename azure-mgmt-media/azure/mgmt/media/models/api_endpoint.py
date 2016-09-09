# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ApiEndpoint(Model):
    """The properties for a Media Services REST API endpoint.

    :param endpoint: The Media Services REST endpoint.
    :type endpoint: str
    :param major_version: The version of Media Services REST API.
    :type major_version: str
    """ 

    _attribute_map = {
        'endpoint': {'key': 'endpoint', 'type': 'str'},
        'major_version': {'key': 'majorVersion', 'type': 'str'},
    }

    def __init__(self, endpoint=None, major_version=None):
        self.endpoint = endpoint
        self.major_version = major_version
