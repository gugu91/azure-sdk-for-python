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


class ImageTag(Model):
    """ImageTag.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar tag_id: Required.
    :vartype tag_id: str
    :ivar tag_name: Required.
    :vartype tag_name: str
    :ivar created: Required.
    :vartype created: datetime
    """

    _validation = {
        'tag_id': {'required': True, 'readonly': True},
        'tag_name': {'required': True, 'readonly': True},
        'created': {'required': True, 'readonly': True},
    }

    _attribute_map = {
        'tag_id': {'key': 'tagId', 'type': 'str'},
        'tag_name': {'key': 'tagName', 'type': 'str'},
        'created': {'key': 'created', 'type': 'iso-8601'},
    }

    def __init__(self, **kwargs) -> None:
        super(ImageTag, self).__init__(**kwargs)
        self.tag_id = None
        self.tag_name = None
        self.created = None
