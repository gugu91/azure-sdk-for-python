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


class ImagePerformance(Model):
    """Image performance model.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar predictions:
    :vartype predictions:
     list[~azure.cognitiveservices.vision.customvision.training.models.Prediction]
    :ivar id: Required.
    :vartype id: str
    :ivar created: Required.
    :vartype created: datetime
    :ivar width: Required.
    :vartype width: int
    :ivar height: Required.
    :vartype height: int
    :ivar image_uri: Required.
    :vartype image_uri: str
    :ivar thumbnail_uri: Required.
    :vartype thumbnail_uri: str
    :ivar tags:
    :vartype tags:
     list[~azure.cognitiveservices.vision.customvision.training.models.ImageTag]
    :ivar regions:
    :vartype regions:
     list[~azure.cognitiveservices.vision.customvision.training.models.ImageRegion]
    """

    _validation = {
        'predictions': {'readonly': True},
        'id': {'required': True, 'readonly': True},
        'created': {'required': True, 'readonly': True},
        'width': {'required': True, 'readonly': True},
        'height': {'required': True, 'readonly': True},
        'image_uri': {'required': True, 'readonly': True},
        'thumbnail_uri': {'required': True, 'readonly': True},
        'tags': {'readonly': True},
        'regions': {'readonly': True},
    }

    _attribute_map = {
        'predictions': {'key': 'predictions', 'type': '[Prediction]'},
        'id': {'key': 'id', 'type': 'str'},
        'created': {'key': 'created', 'type': 'iso-8601'},
        'width': {'key': 'width', 'type': 'int'},
        'height': {'key': 'height', 'type': 'int'},
        'image_uri': {'key': 'imageUri', 'type': 'str'},
        'thumbnail_uri': {'key': 'thumbnailUri', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '[ImageTag]'},
        'regions': {'key': 'regions', 'type': '[ImageRegion]'},
    }

    def __init__(self, **kwargs) -> None:
        super(ImagePerformance, self).__init__(**kwargs)
        self.predictions = None
        self.id = None
        self.created = None
        self.width = None
        self.height = None
        self.image_uri = None
        self.thumbnail_uri = None
        self.tags = None
        self.regions = None
